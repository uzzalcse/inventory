# from django.contrib import admin
# from .models import Location, Accommodation, LocalizedAccommodation
# from leaflet.admin import LeafletGeoAdmin



# class LocationAdmin(LeafletGeoAdmin):
#     list_display = ('id', 'title', 'location_type', 'country_code', 'created_at', 'center')
#     search_fields = ('title', 'country_code')


# class AccommodationAdmin(LeafletGeoAdmin):
#     list_display = ('id', 'title', 'country_code', 'bedroom_count', 'review_score', 'published')
#     search_fields = ('title', 'country_code')
#     list_filter = ('published', 'country_code')


# class LocalizedAccommodationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'property', 'language')
#     search_fields = ('property__title', 'language')


# admin.site.register(Location, LocationAdmin)
# admin.site.register(Accommodation, AccommodationAdmin)
# admin.site.register(LocalizedAccommodation, LocalizedAccommodationAdmin)




# from django.contrib import admin
# from .models import Location, Accommodation, LocalizedAccommodation
# from leaflet.admin import LeafletGeoAdmin

# # Location Admin Configuration
# class LocationAdmin(LeafletGeoAdmin):
#     list_display = ('id', 'title', 'location_type', 'country_code', 'created_at', 'center')
#     search_fields = ('title', 'country_code', 'city', 'state_abbr')
#     list_filter = ('location_type', 'country_code', 'parent')
#     ordering = ('title',)
    
#     # You can also customize the form to use the map widget from Leaflet for the `center` field if needed.
#     fieldsets = (
#         (None, {
#             'fields': ('id', 'title', 'center', 'parent', 'location_type', 'country_code', 'state_abbr', 'city')
#         }),
#         # ('Timestamp', {
#         #     'fields': ('created_at', 'updated_at'),
#         #     'classes': ('collapse',),
#         # }),
#     )

# # Accommodation Admin Configuration
# class AccommodationAdmin(LeafletGeoAdmin):
#     list_display = ('id', 'title', 'user', 'country_code', 'bedroom_count', 'review_score', 'published', 'usd_rate', 'created_at')
#     search_fields = ('title', 'country_code', 'location__title')
#     list_filter = ('published', 'country_code', 'bedroom_count', 'review_score', 'location')
#     ordering = ('title',)
    
#     fieldsets = (
#         (None, {
#             'fields': ('id', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'center', 'location', 'images', 'amenities', 'user', 'published')
#         }),
#         # ('Timestamp', {
#         #     'fields': ('created_at', 'updated_at'),
#         #     'classes': ('collapse',),
#         # }),
#     )

#     # You can add inlines or modify fieldsets to further optimize the admin form as needed.

# # LocalizedAccommodation Admin Configuration
# class LocalizedAccommodationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'property', 'language', 'description')
#     search_fields = ('property__title', 'language', 'description')
#     list_filter = ('language',)
#     ordering = ('language',)

#     fieldsets = (
#         (None, {
#             'fields': ('property', 'language', 'description', 'policy')
#         }),
#     )

# # Register the models in Django Admin
# admin.site.register(Location, LocationAdmin)
# admin.site.register(Accommodation, AccommodationAdmin)
# admin.site.register(LocalizedAccommodation, LocalizedAccommodationAdmin)


from django.contrib import admin
from django.contrib.auth.models import User
from .models import Location, Accommodation, LocalizedAccommodation
from leaflet.admin import LeafletGeoAdmin

# Location Admin Configuration
class LocationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'title', 'location_type', 'country_code', 'created_at', 'center')
    search_fields = ('title', 'country_code', 'city', 'state_abbr')
    list_filter = ('location_type', 'country_code', 'parent')
    ordering = ('title',)

    fieldsets = (
        (None, {
            'fields': ('id', 'title', 'center', 'parent', 'location_type', 'country_code', 'state_abbr', 'city')
        }),
    )

# Accommodation Admin Configuration
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

    # Optionally, you can also restrict access to the add or change view based on the user
    def has_change_permission(self, request, obj=None):
        if obj is not None:
            return obj.user == request.user  # User can only change accommodations they own
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            return obj.user == request.user  # User can only delete accommodations they own
        return super().has_delete_permission(request, obj)

    def has_add_permission(self, request):
        return super().has_add_permission(request)  # All users can add accommodations

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
admin.site.register(Accommodation, AccommodationAdmin)
admin.site.register(LocalizedAccommodation, LocalizedAccommodationAdmin)
