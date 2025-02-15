# Advance Bites

## Overview

Advance Bites is a comprehensive project designed to demonstrate advanced Django REST framework features, including viewsets, routers, and various serializers. It also includes functionality for generating fake data using Faker.

## Features

- **Viewsets and Routers**: Implementation of Django REST framework viewsets and routers for efficient API management.
- **Serializers**: Demonstrates the use of different serializer fields:
  - `StringRelatedField`
  - `PrimaryKeyRelatedField`
  - `HyperlinkedRelatedField`
  - `HyperlinkedIdentityField`
  - `SlugRelatedField`
  - `SlugField`
- **Nested Serializers**: Examples of nested serializers for complex data structures.
- **Fake Data Generation**: Utilizes Faker to generate fake data for testing and development purposes.

## Project Structure

The project is organized into the following directories and files:

```bash
advance_bites/
│
├── __pycache__/
│   └── __init__.py
│
├── .env
├── asgi.py
├── settings.py
├── urls.py
├── wsgi.py
│
├── serializer_relations/
│   ├── __pycache__/
│   │   └── __init__.py
│   │
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── seed.py
│   │   ├── serializer.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── .gitignore
│   ├── db.sqlite3
│   └── manage.py
│
├── README.md
└── requirements.txt
```

## Installation

# Clone the repository
git clone <repository_url>
cd advance_bites

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver

## Usage

### Generating Fake Data

- Use the seed.py script to generate fake data for testing
- ```python manage.py runscript seed```

#### API Endpoints
- Access the API endpoints defined in urls.py to interact with the application

#### Example:
- ```curl http://127.0.0.1:8000/api/your-endpoint/```
