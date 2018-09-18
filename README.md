# Mock Cab

## Overview

A restful web service written in Django to mock a Cab/Taxi backend.

## Installation

In a Python3 environment, preferably a virtual one, execute the following in terminal or command prompt to install the dependencies:

```
pip install -r requirements.txt
```

## Project setup

### Initialize the Database
From the project directory where manage.py resides execute the following in terminal or a command prompt to initialize the database.

```
python manage.py makemigrations
python manage.py migrate
```

### Create an Admin/Superuser

From the project directory execute the following in terminal or a command prompt.
```
python manage.py createsuperuser
```

## Run the project

From the project directory execute the following in terminal or a command prompt. Henceforth, login via the admin user at `localhost:8000/admin` to view the databases.

```
python manage.py runserver
```

## API Endpoints

- /api/**accounts**
- /api/**accounts**/create
- /api/**accounts**/account/{account-id}
- /api/**cabs**
- /api/**cabs**/create
- /api/**cabs**/{cab-id}
- /api/**cabs**/{cab-id}/update
- /api/**trips**
- /api/**trips**/create
- /api/**trips**/trip/{trip-id}
- /api/**trips**/trip/{trip-id}/start
- /api/**trips**/trip/{trip-id}/end

It is recommended to use Django >= 2.1.1 since it supports Browsable API. API parameters and methods allowed are displayed with the same.

## Improvements

Django offers authentication models and permission classes including object level permissions. These functionalities should be added going further to simulate a real world cab service.
