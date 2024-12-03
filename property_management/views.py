
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .forms import PropertyOwnerSignUpForm
from .models import User  # Make sure to import the User model
from django.contrib.auth import logout

def property_owner_signup(request):
    if request.method == 'POST':
        form = PropertyOwnerSignUpForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            
            # Check if the email is already taken
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already in use. Please choose a different one.')
            else:
                try:
                    form.save()  # Try saving the form data to the database
                    return redirect('success')  # Redirect after successful form submission
                except IntegrityError as e:
                    if 'duplicate key value violates unique constraint' in str(e):
                        form.add_error('username', 'This username is already taken. Please choose a different one.')
                
    else:
        form = PropertyOwnerSignUpForm()

    return render(request, 'signup.html', {'form': form})


def success_view(request):
    logout(request)
    return render(request, 'success.html')
