import pytest
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite
from property_management.admin import AccommodationAdmin
from property_management.models import Accommodation, Location
from django.contrib.gis.geos import Point
from unittest.mock import Mock

@pytest.fixture
def superuser(db):
    """Fixture to create a superuser."""
    return User.objects.create_superuser(username="admin", email="admin@example.com", password="password")

@pytest.fixture
def regular_user(db):
    """Fixture to create a regular user."""
    return User.objects.create_user(username="user", email="user@example.com", password="password")

@pytest.fixture
def location(db):
    """Fixture to create a location."""
    return Location.objects.create(
        id="LOC123",
        title="Test Location",
        center=Point(1.0, 1.0),
        location_type="city",
        country_code="US",
    )

@pytest.fixture
def accommodation(db, location, regular_user):
    """Fixture to create an accommodation."""
    return Accommodation.objects.create(
        id="ACC123",
        title="Test Accommodation",
        center=Point(2.0, 2.0),
        country_code="US",
        bedroom_count=3,
        review_score=4.5,
        usd_rate=100.0,
        images=['image1.jpg', 'image2.jpg'],
        amenities={'wifi': True, 'parking': False},
        location=location,
        user=regular_user,
        published=True,
    )

@pytest.fixture
def accommodation_admin():
    """Fixture to create an AccommodationAdmin instance."""
    site = AdminSite()
    return AccommodationAdmin(Accommodation, site)


# Test: has_change_permission for regular user
@pytest.mark.django_db
def test_has_change_permission_regular_user(accommodation_admin, accommodation, regular_user, rf):
    request = rf.get("/")
    request.user = regular_user

    assert accommodation_admin.has_change_permission(request, accommodation) is True


# Test: has_delete_permission for regular user
@pytest.mark.django_db
def test_has_delete_permission_regular_user(accommodation_admin, accommodation, regular_user, rf):
    request = rf.get("/")
    request.user = regular_user

    assert accommodation_admin.has_delete_permission(request, accommodation) is False


# Test: has_delete_permission for superuser
@pytest.mark.django_db
def test_has_delete_permission_superuser(accommodation_admin, accommodation, superuser, rf):
    request = rf.get("/")
    request.user = superuser

    assert accommodation_admin.has_delete_permission(request, accommodation) is True
