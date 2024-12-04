
# Property Management System (Inventory Management)

## Overview
This project involves the development of a Property Management System using Django, PostgreSQL, and PostGIS for geospatial data handling. The system allows property owners to manage property information, including locations and accommodations, through a user-friendly Django Admin interface. It supports spatial data for managing locations and offers features such as property listings, user groups, permissions, and the ability to generate a location sitemap.

## Features
- **Django Admin Interface:** Allows easy management of properties and locations.
- **PostGIS Integration:** Enables the use of geospatial data for locations.
- **User Groups and Permissions:** Property Owners can manage their own properties with restricted access.
- **Frontend:** Public-facing sign-up page for property owners.
- **Sitemap Generation:** Command-line utility to generate a `sitemap.json` for country locations.
- **CSV Import:** Ability to import location data via CSV (optional feature).
- **Code Coverage:** Unit tests using `pytest` with over 70% code coverage.

## Project Structure 


📁 inventory/  
├── 📁 mysite/  
│   ├── 📄 __init__.py  
│   ├── 📄 asgi.py  
│   ├── 📄 settings.py  
│   ├── 📄 urls.py  
│   └── 📄 wsgi.py  
│  
├── 📁 property_management/  
│   ├── 📁 management/  
│   │   └── 📁 commands/  
│   │       └── 📄 generate_sitemap.py  
│   │  
│   ├── 📁 migrations/  
│   │  
│   ├── 📁 static/  
│   │  
│   ├── 📁 templates/  
│   │   ├── 📄 signup.html  
│   │   └── 📄 success.html  
│   │  
│   ├── 📁 tests/  
│   │   ├── 📄 __init__.py  
│   │   ├── 📄 test_admin.py  
│   │   ├── 📄 test_models.py  
│   │   └── 📄 test_views.py  
│   │
│   ├── 📄 __init__.py  
│   ├── 📄 admin.py  
│   ├── 📄 apps.py  
│   ├── 📄 forms.py  
│   ├── 📄 models.py  
│   ├── 📄 urls.py  
│   └── 📄 views.py  
│  
├── 📄 .gitignore  
├── 📄 docker-compose.yml  
├── 📄 Dockerfile  
├── 📄 manage.py  
├── 📄 requirements.txt  
├── 📄 README.md  
└── 📄 pytest.ini  
