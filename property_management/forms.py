
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

class PropertyOwnerSignUpForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    phone_number = forms.CharField(max_length=15, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        # Check if the username already exists in the User model
        if User.objects.filter(username=username).exists():
            raise ValidationError('This username is already taken. Please choose a different one.')

        # Validate username using Django's built-in validators
        try:
            User._meta.get_field('username').run_validators(username)
        except ValidationError as e:
            raise ValidationError(f"Invalid username: {', '.join(e.messages)}")
        
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Check if the email already exists in the User model
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already in use. Please choose a different one.')

        # Validate email using Django's built-in validators
        try:
            User._meta.get_field('email').run_validators(email)
        except ValidationError as e:
            raise ValidationError(f"Invalid email: {', '.join(e.messages)}")

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        # Apply Django's built-in password validators
        try:
            password_validation.validate_password(password)
        except ValidationError as e:
            raise ValidationError(f'Password error: {", ".join(e.messages)}')

        return password

    def save(self):
        # Create the user but keep them inactive
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        
        # Assign the user to the "Property Owners" group
        property_owners_group = Group.objects.get(name='Property Owners')
        user.groups.add(property_owners_group)

        # Keep the user inactive
        user.is_active = False
        user.save()

        return user

