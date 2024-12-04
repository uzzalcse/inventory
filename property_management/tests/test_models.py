
import pytest
from django.contrib.auth.models import User
from property_management.models import Location, Accommodation, LocalizedAccommodation
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.gis.geos import Point


@pytest.fixture
def user():
    """Fixture to create a user"""
    return User.objects.create_user(username="testuser", password="password")


@pytest.fixture
def location():
    """Fixture to create a location"""
    return Location.objects.create(
        id="LOC123",
        title="Test Location",
        center=Point(1.0, 1.0),  # A simple point
        location_type="city",
        country_code="US",
    )


@pytest.fixture
def accommodation(location, user):
    """Fixture to create an accommodation"""
    return Accommodation.objects.create(
        id="ACC123",
        feed=1,
        title="Test Accommodation",
        country_code="US",
        bedroom_count=3,
        review_score=4.5,
        usd_rate=100.00,
        center=Point(1.0, 1.0),
        images=['image1.jpg', 'image2.jpg'],
        amenities={'wifi': True, 'parking': False},
        location=location,
        user=user,
        published=True,
    )


@pytest.fixture
def localized_accommodation(accommodation):
    """Fixture to create a localized accommodation"""
    return LocalizedAccommodation.objects.create(
        property=accommodation,
        language="en",
        description="A test description",
        policy={"cancelation": "no refund"},
    )


# Test Location Model
@pytest.mark.django_db
def test_location_str(location):
    """Test the __str__ method of the Location model"""
    assert str(location) == "Test Location"


@pytest.mark.django_db
def test_location_creation(location):
    """Test the creation of the Location model"""
    assert location.id == "LOC123"
    assert location.title == "Test Location"
    assert location.center.x == 1.0  # Longitude
    assert location.center.y == 1.0  # Latitude


@pytest.mark.django_db
def test_location_missing_center():
    """Test that missing center in Location raises validation error"""
    location = Location(id="LOC125", title="Location Without Center", location_type="city", country_code="US")
    with pytest.raises(IntegrityError):
        location.save()


# @pytest.mark.django_db
# def test_location_missing_country_code():
#     """Test that missing country_code in Location raises validation error"""
#     location = Location(id="LOC126", title="Location Without Country", center=Point(1.0, 1.0), location_type="city")
#     with pytest.raises(IntegrityError):
#         location.save()


@pytest.mark.django_db
def test_location_parent_relation(location):
    """Test the parent-child relationship in Location"""
    child_location = Location.objects.create(
        id="LOC127", title="Child Location", center=Point(2.0, 2.0), location_type="suburb", country_code="US", parent=location
    )
    assert child_location.parent == location


# Test Accommodation Model
@pytest.mark.django_db
def test_accommodation_str(accommodation):
    """Test the __str__ method of the Accommodation model"""
    assert str(accommodation) == "Test Accommodation"


@pytest.mark.django_db
def test_accommodation_creation(accommodation):
    """Test the creation of the Accommodation model"""
    assert accommodation.id == "ACC123"
    assert accommodation.title == "Test Accommodation"
    assert accommodation.bedroom_count == 3
    assert accommodation.review_score == 4.5
    assert accommodation.usd_rate == 100.00
    assert accommodation.location.title == "Test Location"


@pytest.mark.django_db
def test_accommodation_amenities_json(accommodation):
    """Test the amenities JSON field"""
    amenities = accommodation.amenities
    assert amenities['wifi'] is True
    assert amenities['parking'] is False


@pytest.mark.django_db
def test_accommodation_images_json(accommodation):
    """Test the images JSON field"""
    images = accommodation.images
    assert len(images) == 2
    assert "image1.jpg" in images
    assert "image2.jpg" in images


@pytest.mark.django_db
def test_accommodation_user(accommodation, user):
    """Test the foreign key relationship between accommodation and user"""
    assert accommodation.user == user


@pytest.mark.django_db
def test_accommodation_missing_user():
    """Test that missing user in Accommodation raises validation error"""
    accommodation = Accommodation(
        id="ACC125",
        feed=1,
        title="Accommodation Without User",
        country_code="US",
        bedroom_count=2,
        review_score=4.5,
        usd_rate=100.00,
        center=Point(2.0, 2.0),
        images=['image1.jpg'],
        amenities={'wifi': True},
        location=None,
        user=None,  # No user assigned
    )
    with pytest.raises(IntegrityError):
        accommodation.save()


@pytest.mark.django_db
def test_accommodation_missing_usd_rate():
    """Test that missing usd_rate in Accommodation raises validation error"""
    accommodation = Accommodation(
        id="ACC126",
        feed=1,
        title="Accommodation Without USD Rate",
        country_code="US",
        bedroom_count=2,
        review_score=4.5,
        center=Point(2.0, 2.0),
        images=['image1.jpg'],
        amenities={'wifi': True},
        location=None,
        user=None,
    )
    with pytest.raises(IntegrityError):
        accommodation.save()


# Test LocalizedAccommodation Model
@pytest.mark.django_db
def test_localized_accommodation_str(localized_accommodation):
    """Test the __str__ method of the LocalizedAccommodation model"""
    assert str(localized_accommodation) == "Test Accommodation (en)"


@pytest.mark.django_db
def test_localized_accommodation_creation(localized_accommodation, accommodation):
    """Test the creation of LocalizedAccommodation"""
    assert localized_accommodation.property == accommodation
    assert localized_accommodation.language == "en"
    assert localized_accommodation.description == "A test description"
    assert localized_accommodation.policy['cancelation'] == "no refund"


@pytest.mark.django_db
def test_localized_accommodation_missing_description():
    """Test that missing description in LocalizedAccommodation raises validation error"""
    localized_accommodation = LocalizedAccommodation(
        property=Accommodation.objects.first(),
        language="en",
        description="",  # Empty description
        policy={"cancelation": "no refund"},
    )
    with pytest.raises(ValidationError):
        localized_accommodation.full_clean()  # Manually trigger validation


@pytest.mark.django_db
def test_localized_accommodation_missing_policy():
    """Test that missing policy in LocalizedAccommodation raises validation error"""
    localized_accommodation = LocalizedAccommodation(
        property=Accommodation.objects.first(),
        language="en",
        description="Test Description",
    )
    with pytest.raises(IntegrityError):
        localized_accommodation.save()


# Test model constraints and validation

@pytest.mark.django_db
def test_accommodation_missing_location():
    """Test that missing location in Accommodation raises validation error"""
    accommodation = Accommodation(
        id="ACC124",
        feed=1,
        title="Invalid Accommodation",
        country_code="US",
        bedroom_count=2,
        review_score=4.5,
        usd_rate=100.00,
        center=Point(2.0, 2.0),
        images=['image1.jpg'],
        amenities={'wifi': True},
        location=None,  # No location assigned
        user=None,  # No user assigned
    )
    with pytest.raises(IntegrityError):
        accommodation.save()
