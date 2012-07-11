#-*- coding: UTF-8 -*-
import os


DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))

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

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'vwz(3e9-zuqf)l-&amp;6srbf7xk*gklc^*ed#=m7=lcq95mkvresz'

# Dominio predeterminado del servidor
#  Ejemplo: '127.0.0.1:8000'
DEFAULT_HOST = '127.0.0.1:8000'
