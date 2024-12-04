
import json
from django.core.management.base import BaseCommand
from property_management.models import Location


class Command(BaseCommand):
    help = 'Generate a JSON sitemap with country/state/city/location structure.'

    def handle(self, *args, **kwargs):
        # Step 1: Fetch all locations
        locations = Location.objects.all()

        # Step 2: Build a dictionary to store locations grouped by country
        location_dict = {}

        for location in locations:
            country_code = location.country_code.upper()

            if country_code not in location_dict:
                location_dict[country_code] = {
                    "name": country_code,
                    "slug": country_code.lower(),
                    "locations": {}
                }

            # Get the full path for a location following country/state/city/location structure
            slug_path = self.get_full_slug(location, country_code)

            # Add location to the dictionary under the correct country
            location_dict[country_code]["locations"][slug_path] = location.title

        # Step 3: Create a sitemap list and sort locations alphabetically by their slug paths
        sitemap = []
        for country in sorted(location_dict.keys()):
            sitemap.append({
                country: location_dict[country]["slug"],
                "locations": [
                    {title: slug} for slug, title in sorted(
                        location_dict[country]["locations"].items(),
                        key=lambda x: x[1].lower()  # Sort by title alphabetically
                    )
                ]
            })

        # Step 4: Save the sitemap to a JSON file
        output_file = 'sitemap.json'
        with open(output_file, 'w') as f:
            json.dump(sitemap, f, indent=4)

        self.stdout.write(self.style.SUCCESS(f'Sitemap generated and saved to {output_file}'))

    def get_full_slug(self, location, country_code):
        """
        Recursively build the full slug path for a location by including parent locations,
        following the structure countrycode/state/city/location.
        """
        # Slugify the location title
        slug_parts = [self.slugify(location.title)]
        parent = location.parent

        # Traverse through parent locations (state -> city -> location)
        while parent:
            # Add the parent's title as part of the slug if it's a location
            slug_parts.insert(0, self.slugify(parent.title))
            parent = parent.parent

        # Include country code as the first part of the slug path
        slug_parts.insert(0, country_code.lower())

        # Return the slug path as `countrycode/state/city/location`
        return '/'.join(slug_parts)

    def slugify(self, title):
        """
        Convert a title to a slug-friendly format:
        - Replace spaces with hyphens
        - Convert to lowercase
        """
        return title.lower().replace(" ", "-")
