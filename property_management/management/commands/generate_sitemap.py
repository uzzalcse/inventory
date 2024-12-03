# import json
# from django.core.management.base import BaseCommand
# from django.utils.text import slugify
# from property_management.models import Location

# class Command(BaseCommand):
#     help = 'Generate a sitemap.json for all country locations'

#     def handle(self, *args, **kwargs):
#         # Fetch all locations, ordered by country_code and title
#         locations = Location.objects.all().order_by('country_code', 'title')

#         # Dictionary to store country data
#         country_dict = {}

#         # Iterate over all locations to group them by country_code
#         for location in locations:
#             country_code = location.country_code
#             location_slug = slugify(location.title)
#             location_url = f"{country_code.lower()}/{location_slug}"

#             # Get the country name using the country_code
#             country_name = self.get_country_name_from_code(country_code)

#             # If the country is not in the dictionary, initialize it
#             if country_code not in country_dict:
#                 country_dict[country_code] = {
#                     "country_name": country_name,
#                     "locations": []
#                 }

#             # Add the location URL and name to the country's location list
#             country_dict[country_code]["locations"].append({
#                 location.title: location_url
#             })

#         # Prepare the output list
#         output = []

#         for country_code, data in country_dict.items():
#             # Sort locations by the title of the location (alphabetically)
#             sorted_locations = sorted(data["locations"], key=lambda x: list(x.keys())[0])

#             # Add country and its sorted locations to the output
#             output.append({
#                 data["country_name"]: country_code.lower(),
#                 "locations": sorted_locations
#             })

#         # Save the output to a JSON file
#         with open('sitemap.json', 'w') as f:
#             json.dump(output, f, indent=4)

#         self.stdout.write(self.style.SUCCESS('Sitemap generated successfully'))

#     def get_country_name_from_code(self, country_code):
#         """
#         Fetch the country name based on the country code.
#         You can implement this function to look up the country name from a model or use an external library like pycountry.
#         """
#         # For now, we assume the country_code itself represents the country name.
#         # You can modify this logic to map country_code to full country names.
#         return country_code  # Modify to return a country name using a model or library if needed


# import json
# from django.core.management.base import BaseCommand
# from django.utils.text import slugify
# from property_management.models import Location

# class Command(BaseCommand):
#     help = 'Generate a sitemap.json for all country locations'

#     def handle(self, *args, **kwargs):
#         # Fetch all locations, ordered by country_code, city, and title
#         locations = Location.objects.all().order_by('country_code', 'city', 'title')

#         # Dictionary to store country data
#         country_dict = {}

#         # Iterate over all locations to group them by country_code
#         for location in locations:
#             country_code = location.country_code
#             location_slug = slugify(location.title)
#             location_path = f"{country_code.lower()}/{slugify(location.city)}/{location_slug}"

#             # Get the country name using the country_code
#             country_name = self.get_country_name_from_code(country_code)

#             # If the country is not in the dictionary, initialize it
#             if country_code not in country_dict:
#                 country_dict[country_code] = {
#                     "country_name": country_name,
#                     "locations": []
#                 }

#             # Add the location URL and name to the country's location list
#             country_dict[country_code]["locations"].append({
#                 location.title: location_path
#             })

#         # Prepare the output list
#         output = []

#         for country_code, data in country_dict.items():
#             # Sort locations by the title of the location (alphabetically)
#             sorted_locations = sorted(data["locations"], key=lambda x: list(x.keys())[0])

#             # Add country and its sorted locations to the output
#             output.append({
#                 data["country_name"]: country_code.lower(),
#                 "locations": sorted_locations
#             })

#         # Save the output to a JSON file
#         with open('sitemap.json', 'w') as f:
#             json.dump(output, f, indent=4)

#         self.stdout.write(self.style.SUCCESS('Sitemap generated successfully'))

#     def get_country_name_from_code(self, country_code):
#         """
#         Fetch the country name based on the country code.
#         You can implement this function to look up the country name from a model or use an external library like pycountry.
#         """
#         # For now, we assume the country_code itself represents the country name.
#         # You can modify this logic to map country_code to full country names.
#         return country_code  # Modify to return a country name using a model or library if needed


# import json
# from django.core.management.base import BaseCommand
# from django.utils.text import slugify
# from property_management.models import Location

# class Command(BaseCommand):
#     help = 'Generate a sitemap.json for all country locations'

#     def handle(self, *args, **kwargs):
#         # Fetch all locations, ordered by country_code, city, and title
#         locations = Location.objects.all().order_by('country_code', 'city', 'title')

#         # Dictionary to store country data
#         country_dict = {}

#         # Iterate over all locations to group them by country_code
#         for location in locations:
#             country_code = location.country_code
#             location_slug = slugify(location.title)
#             location_path = self.create_location_path(location, country_code)

#             # Get the country name using the country_code
#             country_name = self.get_country_name_from_code(country_code)

#             # If the country is not in the dictionary, initialize it
#             if country_code not in country_dict:
#                 country_dict[country_code] = {
#                     "country_name": country_name,
#                     "locations": []
#                 }

#             # Add the location URL and name to the country's location list
#             country_dict[country_code]["locations"].append({
#                 location.title: location_path
#             })

#         # Prepare the output list
#         output = []

#         for country_code, data in country_dict.items():
#             # Sort locations by the title of the location (alphabetically)
#             sorted_locations = sorted(data["locations"], key=lambda x: list(x.keys())[0])

#             # Add country and its sorted locations to the output
#             output.append({
#                 data["country_name"]: country_code.lower(),
#                 "locations": sorted_locations
#             })

#         # Save the output to a JSON file
#         with open('sitemap.json', 'w') as f:
#             json.dump(output, f, indent=4)

#         self.stdout.write(self.style.SUCCESS('Sitemap generated successfully'))

#     def create_location_path(self, location, country_code):
#         """
#         Creates a hierarchical path for the location from root to the top (country -> city -> subcity).
#         """
#         # Start with the country and city
#         path = f"{country_code.lower()}/{slugify(location.city)}"

#         # Add the location itself, creating a path like "bd/dhaka/banani"
#         path += f"/{slugify(location.title)}"

#         return path

#     def get_country_name_from_code(self, country_code):
#         """
#         Fetch the country name based on the country code.
#         You can implement this function to look up the country name from a model or use an external library like pycountry.
#         """
#         # For now, we assume the country_code itself represents the country name.
#         # You can modify this logic to map country_code to full country names.
#         return country_code  # Modify to return a country name using a model or library if needed


# import json
# from django.core.management.base import BaseCommand
# from django.utils.text import slugify
# from property_management.models import Location

# class Command(BaseCommand):
#     help = 'Generate a sitemap.json for all country locations'

#     def handle(self, *args, **kwargs):
#         # Fetch all locations, ordered by country_code, city, and title
#         locations = Location.objects.all().order_by('country_code', 'city', 'title')

#         # Dictionary to store country data
#         country_dict = {}

#         # Iterate over all locations to group them by country_code
#         for location in locations:
#             country_code = location.country_code
#             location_slug = slugify(location.title)
#             location_path = self.create_location_path(location, country_code)

#             # Get the country name using the country_code
#             country_name = self.get_country_name_from_code(country_code)

#             # If the country is not in the dictionary, initialize it
#             if country_code not in country_dict:
#                 country_dict[country_code] = {
#                     "country_name": country_name,
#                     "locations": []
#                 }

#             # Add the location URL and name to the country's location list
#             country_dict[country_code]["locations"].append({
#                 location.title: location_path
#             })

#         # Prepare the output list
#         output = []

#         for country_code, data in country_dict.items():
#             # Sort locations by the title of the location (alphabetically)
#             sorted_locations = sorted(data["locations"], key=lambda x: list(x.keys())[0])

#             # Add country and its sorted locations to the output
#             output.append({
#                 data["country_name"]: country_code.lower(),
#                 "locations": sorted_locations
#             })

#         # Save the output to a JSON file
#         with open('sitemap.json', 'w') as f:
#             json.dump(output, f, indent=4)

#         self.stdout.write(self.style.SUCCESS('Sitemap generated successfully'))

#     def create_location_path(self, location, country_code):
#         """
#         Creates a hierarchical path for the location from root to the top (country -> city -> location).
#         If no city is specified, it uses the country as the subroot.
#         """
#         # Start with the country
#         path = f"{country_code.lower()}"

#         # If city is available, include it
#         if location.city:
#             path += f"/{slugify(location.city)}"
#         else:
#             # If no city, use the country as the subroot
#             path += f"/none"  # This can be a placeholder like "none" for general locations

#         # Add the location itself, creating a path like "bd/dhaka/banani"
#         path += f"/{slugify(location.title)}"

#         return path

#     def get_country_name_from_code(self, country_code):
#         """
#         Fetch the country name based on the country code.
#         You can implement this function to look up the country name from a model or use an external library like pycountry.
#         """
#         # For now, we assume the country_code itself represents the country name.
#         # You can modify this logic to map country_code to full country names.
#         return country_code  # Modify to return a country name using a model or library if needed


# import json
# from django.core.management.base import BaseCommand
# from django.utils.text import slugify
# from property_management.models import Location

# class Command(BaseCommand):
#     help = 'Generate a sitemap.json for all country locations'

#     def handle(self, *args, **kwargs):
#         # Fetch all locations, ordered by country_code, city, and title
#         locations = Location.objects.all().order_by('country_code', 'city', 'title')

#         # Dictionary to store country data
#         country_dict = {}

#         # Iterate over all locations to group them by country_code
#         for location in locations:
#             country_code = location.country_code
#             location_slug = slugify(location.title)
#             city_slug = slugify(location.city) if location.city else 'none'
#             location_path = f"{country_code.lower()}/{city_slug}/{location_slug}"

#             # Get the country name using the country_code
#             country_name = self.get_country_name_from_code(country_code)

#             # If the country is not in the dictionary, initialize it
#             if country_name not in country_dict:
#                 country_dict[country_name] = {
#                     "country_code": country_code,
#                     "locations": []
#                 }

#             # Add the location URL and name to the country's location list
#             country_dict[country_name]["locations"].append({
#                 location.title: location_path
#             })

#         # Prepare the output list
#         output = []

#         for country_name, data in country_dict.items():
#             # Sort locations by the title of the location (alphabetically)
#             sorted_locations = sorted(data["locations"], key=lambda x: list(x.keys())[0])

#             # Add country and its sorted locations to the output
#             output.append({
#                 country_name: data["country_code"],
#                 "locations": sorted_locations
#             })

#         # Save the output to a JSON file
#         with open('sitemap.json', 'w') as f:
#             json.dump(output, f, indent=4)

#         self.stdout.write(self.style.SUCCESS('Sitemap generated successfully'))

#     def get_country_name_from_code(self, country_code):
#         """
#         Fetch the country name based on the country code.
#         You can implement this function to look up the country name from a model or use an external library like pycountry.
#         """
#         # For now, we assume the country_code itself represents the country name.
#         # You can modify this logic to map country_code to full country names.
#         return country_code  # Modify to return a country name using a model or library if needed


# import json
# from django.core.management.base import BaseCommand
# from django.utils.text import slugify
# from property_management.models import Location

# class Command(BaseCommand):
#     help = 'Generate a sitemap.json for all country locations'

#     def handle(self, *args, **kwargs):
#         # Fetch all locations, ordered by country_code, city, and title
#         locations = Location.objects.all().order_by('country_code', 'city', 'title')

#         # Dictionary to store country data
#         country_dict = {}

#         # Iterate over all locations to group them by country_code
#         for location in locations:
#             country_code = location.country_code
#             location_slug = slugify(location.title)
#             city_slug = slugify(location.city) if location.city else 'none'

#             # Building the path from location to root (country)
#             location_path = self.build_location_path(location, country_code)

#             # Get the country name using the country_code
#             country_name = self.get_country_name_from_code(country_code)

#             # If the country is not in the dictionary, initialize it
#             if country_name not in country_dict:
#                 country_dict[country_name] = {
#                     "country_code": country_code,
#                     "locations": []
#                 }

#             # Add the location URL and name to the country's location list
#             country_dict[country_name]["locations"].append({
#                 location.title: location_path
#             })

#         # Prepare the output list
#         output = []

#         for country_name, data in country_dict.items():
#             # Sort locations by the title of the location (alphabetically)
#             sorted_locations = sorted(data["locations"], key=lambda x: list(x.keys())[0])

#             # Add country and its sorted locations to the output
#             output.append({
#                 country_name: data["country_code"],
#                 "locations": sorted_locations
#             })

#         # Save the output to a JSON file
#         with open('sitemap.json', 'w') as f:
#             json.dump(output, f, indent=4)

#         self.stdout.write(self.style.SUCCESS('Sitemap generated successfully'))

#     def build_location_path(self, location, country_code):
#         """
#         Build the full path from the location up to the root (country).
#         This method traverses from the location to its parent city, then to the country.
#         """
#         path_parts = [country_code.lower()]  # Start with the country code

#         if location.city:
#             city_slug = slugify(location.city)
#             path_parts.append(city_slug)  # Add the city if available

#         location_slug = slugify(location.title)
#         path_parts.append(location_slug)  # Add the location itself

#         return '/'.join(path_parts)

#     def get_country_name_from_code(self, country_code):
#         """
#         Fetch the country name based on the country code.
#         You can implement this function to look up the country name from a model or use an external library like pycountry.
#         """
#         # For now, we assume the country_code itself represents the country name.
#         # You can modify this logic to map country_code to full country names.
#         return country_code  # Modify to return a country name using a model or library if needed



# import json
# from django.core.management.base import BaseCommand
# from django.utils.text import slugify
# from property_management.models import Location

# class Command(BaseCommand):
#     help = 'Generate a sitemap.json for all country locations'

#     def handle(self, *args, **kwargs):
#         # Fetch all locations
#         locations = Location.objects.all().order_by('country_code', 'city', 'title')

#         # Dictionary to store country data
#         country_dict = {}

#         # Iterate over all locations to group them by country_code
#         for location in locations:
#             country_code = location.country_code

#             # Building the path from location to root (country)
#             location_path = self.build_location_path(location)

#             # Get the country name using the country_code
#             country_name = self.get_country_name_from_code(country_code)

#             # If the country is not in the dictionary, initialize it
#             if country_name not in country_dict:
#                 country_dict[country_name] = {
#                     "country_code": country_code,
#                     "locations": []
#                 }

#             # Add the location URL and name to the country's location list
#             country_dict[country_name]["locations"].append({
#                 location.title: location_path
#             })

#         # Prepare the output list
#         output = []

#         for country_name, data in country_dict.items():
#             # Sort locations by the title of the location (alphabetically)
#             sorted_locations = sorted(data["locations"], key=lambda x: list(x.keys())[0])

#             # Add country and its sorted locations to the output
#             output.append({
#                 country_name: data["country_code"],
#                 "locations": sorted_locations
#             })

#         # Save the output to a JSON file
#         with open('sitemap.json', 'w') as f:
#             json.dump(output, f, indent=4)

#         self.stdout.write(self.style.SUCCESS('Sitemap generated successfully'))

#     def build_location_path(self, location):
#         """
#         Build the full path from the location up to the root (country).
#         This method traverses from the location to its parent, then to the root country.
#         """
#         path_parts = []
#         current_location = location

#         # Traverse upwards from the location to the root using the parent field
#         while current_location:
#             location_slug = slugify(current_location.title)
#             path_parts.append(location_slug)

#             # Move to the parent location
#             current_location = current_location.parent

#         # Reverse the path to go from root to location
#         path_parts.reverse()

#         # Join the path parts with slashes
#         return '/'.join(path_parts)

#     def get_country_name_from_code(self, country_code):
#         """
#         Fetch the country name based on the country code.
#         You can implement this function to look up the country name from a model or use an external library like pycountry.
#         """
#         # For now, we assume the country_code itself represents the country name.
#         return country_code  # Modify to return a country name using a model or library if needed

import json
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from property_management.models import Location

class Command(BaseCommand):
    help = 'Generate a sitemap.json for all country locations'

    def handle(self, *args, **kwargs):
        # Fetch all locations, ordered by country_code, city, and title
        locations = Location.objects.all().order_by('country_code', 'city', 'title')

        # Dictionary to store country data
        country_dict = {}

        # Iterate over all locations to group them by country_code
        for location in locations:
            country_code = location.country_code

            # Building the path from location to root (country)
            location_path = self.build_location_path(location)

            # Get the country name using the country_code
            country_name = self.get_country_name_from_code(country_code)

            # If the country is not in the dictionary, initialize it
            if country_name not in country_dict:
                country_dict[country_name] = {
                    "country_code": country_code,
                    "locations": []
                }

            # Add the location URL and name to the country's location list
            country_dict[country_name]["locations"].append({
                location.title: location_path
            })

        # Prepare the output list
        output = []

        for country_name, data in country_dict.items():
            # Sort locations by the title of the location (alphabetically)
            sorted_locations = sorted(data["locations"], key=lambda x: list(x.keys())[0])

            # Add country and its sorted locations to the output
            output.append({
                country_name: data["country_code"],
                "locations": sorted_locations
            })

        # Save the output to a JSON file
        with open('sitemap.json', 'w') as f:
            json.dump(output, f, indent=4)

        self.stdout.write(self.style.SUCCESS('Sitemap generated successfully'))

    def build_location_path(self, location):
        """
        Build the full path from the location up to the root (country).
        This method starts with the country code and then traverses up through parent locations.
        """
        path_parts = [location.country_code.lower()]  # Start with the country code

        current_location = location

        # Traverse upwards from the location to the root using the parent field
        while current_location:
            location_slug = slugify(current_location.title)
            path_parts.append(location_slug)  # Add the current location to the path

            # Move to the parent location
            current_location = current_location.parent

        # Join the path parts with slashes (no need to reverse since country code is first)
        return '/'.join(path_parts)

    def get_country_name_from_code(self, country_code):
        """
        Fetch the country name based on the country code.
        You can implement this function to look up the country name from a model or use an external library like pycountry.
        """
        # For now, we assume the country_code itself represents the country name.
        return country_code  # Modify to return a country name using a model or library if needed
