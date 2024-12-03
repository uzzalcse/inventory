from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.property_owner_signup, name='signup'),
    path('success/', views.success_view, name='success'),
]