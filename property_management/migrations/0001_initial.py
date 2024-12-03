# Generated by Django 5.1.3 on 2024-12-03 04:38

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('feed', models.PositiveSmallIntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=2)),
                ('bedroom_count', models.PositiveIntegerField()),
                ('review_score', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('usd_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('center', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('images', models.JSONField()),
                ('amenities', models.JSONField()),
                ('published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LocalizedAccommodation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=2)),
                ('description', models.TextField()),
                ('policy', models.JSONField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localizations', to='property_management.accommodation')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('center', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('location_type', models.CharField(max_length=20)),
                ('country_code', models.CharField(max_length=2)),
                ('state_abbr', models.CharField(blank=True, max_length=3, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='property_management.location')),
            ],
        ),
        migrations.AddField(
            model_name='accommodation',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accommodations', to='property_management.location'),
        ),
    ]
