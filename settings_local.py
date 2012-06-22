#-*- coding: UTF-8 -*-
import os

PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

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

# Django Social Auth
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.contrib.orkut.OrkutBackend',
    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.vkontakte.VkontakteBackend',
#    'social_auth.backends.contrib.live.LiveBackend',
#    'social_auth.backends.contrib.skyrock.SkyrockBackend',
#    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Django Social Auth: OAuth Keys, availabel from:
#    http://www.facebook.com/developers/createapp.php
#    https://developer.yahoo.com/dashboard/createKey.html
#    https://www.google.com/accounts/ManageDomains
#    http://twitter.com/oauth_clients

# Aplicacion Twitter para pruebas mantenida por
#  Jesús Hernández Gormaz <jhg.jesus@gmail.com>
# Nombre de la aplicación: SEW Test
# Descripcion: Pruebas en el desarrollo de SEW
# Web: http://127.0.0.1:8000/
# Acceso: Solo lectura
# URL de llamada atras: http://127.0.0.1:8000/admin/
# Consumer key: WgC13BNFq9ubWLuzVxR3yA
# Consumer secret: FDJiopJJCPyEqhxikvWGm2PgUzJql7pY2ENt7cbOF0
TWITTER_CONSUMER_KEY = 'WgC13BNFq9ubWLuzVxR3yA'
TWITTER_CONSUMER_SECRET = 'FDJiopJJCPyEqhxikvWGm2PgUzJql7pY2ENt7cbOF0'
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''
DROPBOX_APP_ID = ''
DROPBOX_API_SECRET = ''
EVERNOTE_CONSUMER_KEY = ''
EVERNOTE_CONSUMER_SECRET = ''
LINKEDIN_CONSUMER_KEY = ''
LINKEDIN_CONSUMER_SECRET = ''
ORKUT_CONSUMER_KEY = ''
ORKUT_CONSUMER_SECRET = ''
GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''
GOOGLE_CONSUMER_KEY = ''
GOOGLE_CONSUMER_SECRET = ''
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''
FOURSQUARE_CONSUMER_KEY = ''
FOURSQUARE_CONSUMER_SECRET = ''
VK_APP_ID = ''
VK_API_SECRET = ''
LIVE_CLIENT_ID = ''
LIVE_CLIENT_SECRET = ''
SKYROCK_CONSUMER_KEY = ''
SKYROCK_CONSUMER_SECRET = ''
YAHOO_CONSUMER_KEY = ''
YAHOO_CONSUMER_SECRET = ''

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

# Host donde esta alojado SEW
HOST = '127.0.0.1:8000'

# Alojamiento de los archivos subidos
MEDIA_HOST = '//' + HOST + '/'

# Alojamiento de los archivos estaticos
STATIC_HOST = '//' + HOST + '/'
