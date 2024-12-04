import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import Client

@pytest.fixture
def client():
    """Fixture to return a Django test client."""
    return Client()


@pytest.fixture
def user_data():
    """Fixture to provide user data for form submission."""
    return {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password1': 'strongpassword123',
        'password2': 'strongpassword123'
    }


@pytest.mark.django_db
def test_property_owner_signup_success(client, user_data):
    """Test successful property owner signup."""
    response = client.post(reverse('signup'), data=user_data)

    assert response.status_code == 200  # Successful form submission should redirect



@pytest.mark.django_db
def test_property_owner_signup_duplicate_email(client, user_data):
    """Test property owner signup with a duplicate email."""
    User.objects.create_user(username='existinguser', email=user_data['email'], password='password')

    response = client.post(reverse('signup'), data=user_data)

    assert response.status_code == 200  # Should return the form page with an error
    assert User.objects.filter(username='testuser').exists() is False  # New user should not be created
    assert 'This email is already in use' in response.content.decode()  # Check error message


@pytest.mark.django_db
def test_property_owner_signup_duplicate_username(client, user_data):
    """Test property owner signup with a duplicate username."""
    User.objects.create_user(username='testuser', email='different@example.com', password='password')

    response = client.post(reverse('signup'), data=user_data)

    assert response.status_code == 200  # Should return the form page with an error
    assert User.objects.filter(email=user_data['email']).exists() is False  # New user should not be created
    assert 'This username is already taken' in response.content.decode()  # Check error message


@pytest.mark.django_db
def test_property_owner_signup_invalid_password(client, user_data):
    """Test property owner signup with invalid passwords."""
    user_data['password1'] = 'short'
    user_data['password2'] = 'short'

    response = client.post(reverse('signup'), data=user_data)

    assert response.status_code == 200  # Should return the form page with an error
    assert User.objects.filter(username='testuser').exists() is False  # User should not be created

