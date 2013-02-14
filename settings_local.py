#-*- coding: UTF-8 -*-
import os


# En producción esta variable debe ser falsa por seguridad
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Ruta al proyecto: NO MODIFICAR
PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))

# Nombres y correos de los administradores del sitio
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': PROJECT_DIR + '/sew.sqlite',  # Usa PROJECT_DIR + 'nombre'
                                              #  para SQLite
        # Not used with sqlite3.
        'USER': '',
        # Not used with sqlite3.
        'PASSWORD': '',
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',
        # Set to empty string for default. Not used with sqlite3.
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Atlantic/Canary'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-es'

# First day of week, 0 for Sunday, 1 Monday, etc.
FIRST_DAY_OF_WEEK = 1

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 1000,
        }
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'iwv!am3+-k@2=lg5#(8o9h=zpa(degh-k%5z*pc1tk&amp;a!16&amp;=f'
