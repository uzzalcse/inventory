
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Location, Accommodation, LocalizedAccommodation
from leaflet.admin import LeafletGeoAdmin


#Location with import and export 

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Location
from leaflet.admin import LeafletGeoAdmin

# 1. Define a Resource class for the Location model
class LocationResource(resources.ModelResource):
    class Meta:
        model = Location
        fields = ('id', 'title', 'location_type', 'country_code', 'state_abbr', 'city', 'center')  # Adjust fields as necessary

# 2. Modify LocationAdmin to use ImportExportModelAdmin
class LocationAdmin(ImportExportModelAdmin, LeafletGeoAdmin):
    resource_class = LocationResource  # Specify the resource class
    list_display = ('id', 'title', 'location_type', 'country_code', 'created_at', 'center')
    search_fields = ('title', 'country_code', 'city', 'state_abbr')
    list_filter = ('location_type', 'country_code', 'parent')
    ordering = ('title',)

    fieldsets = (
        (None, {
            'fields': ('id', 'title', 'center', 'parent', 'location_type', 'country_code', 'state_abbr', 'city')
        }),
    )





# LocalizedAccommodation Admin Configuration
class LocalizedAccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'property', 'language', 'description')
    search_fields = ('property__title', 'language', 'description')
    list_filter = ('language',)
    ordering = ('language',)

    fieldsets = (
        (None, {
            'fields': ('property', 'language', 'description', 'policy')
        }),
    )

# Register the models in Django Admin
admin.site.register(Location, LocationAdmin)
# admin.site.register(Accommodation, AccommodationAdmin)
admin.site.register(LocalizedAccommodation, LocalizedAccommodationAdmin)


# #from here accomodation code starts

from django.contrib import admin
from .models import Accommodation
from leaflet.admin import LeafletGeoAdmin

class AccommodationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'title', 'user', 'country_code', 'bedroom_count', 'review_score', 'published', 'usd_rate', 'created_at')
    search_fields = ('title', 'country_code', 'location__title')
    list_filter = ('published', 'country_code', 'bedroom_count', 'review_score', 'location')
    ordering = ('title',)

    fieldsets = (
        (None, {
            'fields': ('id', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'center', 'location', 'images', 'amenities', 'user', 'published')
        }),
    )

    # Filter queryset to show only accommodations that belong to the logged-in user
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset  # Superusers can see all accommodations
        return queryset.filter(user=request.user)  # Regular users can only see their own accommodations

    # Restrict permission to change only accommodations owned by the logged-in user
    def has_change_permission(self, request, obj=None):
        if obj is not None:
            return obj.user == request.user  # User can only change accommodations they own
        return super().has_change_permission(request, obj)

    # Restrict permission to delete only accommodations owned by the logged-in user (for regular users)
    # Allow superusers to delete any accommodation
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True  # Allow superuser to delete any accommodation
        return False  # Regular users cannot delete any accommodation

    def has_add_permission(self, request):
        return super().has_add_permission(request)  # All users can add accommodations

    # Override the get_form method to pass the current user and disable the field for non-superusers
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Check if the 'user' field is in the form fields before modifying it
        if 'user' in form.base_fields:
            if not obj:  # When adding a new accommodation
                if request.user.is_superuser:
                    # Superusers can choose any user
                    form.base_fields['user'].queryset = form.base_fields['user'].queryset.all()
                else:
                    # Non-superusers should have their user set automatically and disabled
                    form.base_fields['user'].initial = request.user
                    form.base_fields['user'].disabled = True
            else:
                # Disable the user field during edits
                form.base_fields['user'].disabled = True

        return form

    # Override the save_model method to automatically set the user field for non-superusers
    def save_model(self, request, obj, form, change):
        if not change:  # Only set the user if it's a new object
            if not obj.user:
                obj.user = request.user  # Set the user to the current user if not set
        super().save_model(request, obj, form, change)

# Register the model with the custom admin class
admin.site.register(Accommodation, AccommodationAdmin)




