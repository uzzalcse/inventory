from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.timezone import now


# Location Model
class Location(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=100)
    center = gis_models.PointField(geography=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )
    location_type = models.CharField(max_length=20)
    country_code = models.CharField(max_length=2)
    state_abbr = models.CharField(max_length=3, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Accommodation Model
class Accommodation(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    feed = models.PositiveSmallIntegerField(default=0)
    title = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)
    bedroom_count = models.PositiveIntegerField()
    review_score = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    usd_rate = models.DecimalField(max_digits=10, decimal_places=2)
    center = gis_models.PointField(geography=True)
    images = models.JSONField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='accommodations')
    amenities = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Localized Accommodation Model
class LocalizedAccommodation(models.Model):
    id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='localizations')
    language = models.CharField(max_length=2)
    description = models.TextField()
    policy = models.JSONField()

    def __str__(self):
        return f'{self.property.title} ({self.language})'



