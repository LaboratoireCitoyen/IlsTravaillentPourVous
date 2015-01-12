"""
Django settings for ilstravaillentpourvous project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from django.conf.global_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__) + '/../..')

BOWER_INSTALLED_APPS = (
    'jquery',
    'foundation',
    'html5shiv',
    'respond',
    'less',
)

def project_directory(*join):
    return os.path.realpath(
        os.path.join(BASE_DIR, *join).replace('\\', '/'))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@8i3i1u#awhq%x2jkpu^ggi#mwso92+h8x7as&$$s3k1@x$eds'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

TEMPLATE_DEBUG = os.environ.get('TEMPLATE_DEBUG', DEBUG)

ALLOWED_HOSTS = []

PIPELINE_CSS = {
    'style': {
        'source_filenames': (
            'foundation/css/normalize.css',
            'foundation/css/foundation.css',
            'autocomplete_light/style.css',
        ),
        'output_filename': 'css/style.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'script': {
        'source_filenames': (
            'autocomplete_light/autocomplete.js',
            'autocomplete_light/widget.js',
            'autocomplete_light/addanother.js',
            'autocomplete_light/text_widget.js',
            'autocomplete_light/remote.js',
            'respond/dest/respond.src.js',
            'modernizr/modernizr.js',
            'html5shiv/dist/html5shiv.js',
            'foundation/js/foundation.js',
        ),
        'output_filename': 'js/script.js',
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djangobower',
    'pipeline',
    'autocomplete_light',

    'deputes',
    'dossiers',
    'groupes',
    'scrutins',
    'votes',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ilstravaillentpourvous.urls'

WSGI_APPLICATION = 'ilstravaillentpourvous.wsgi.application'

STATICFILES_FINDERS += (
    'djangobower.finders.BowerFinder',
    'pipeline.finders.PipelineFinder',
)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sc',
        'USER': 'sc',
        'PASSWORD': 'sc',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = project_directory('public/media')
MEDIA_URL = '/public/media/'
STATIC_ROOT = project_directory('public/static')
STATIC_URL = '/public/static/'
STATICFILES_DIRS = (project_directory('static'),)
TEMPLATE_DIRS = (project_directory('templates'),)
FIXTURE_DIRS = (project_directory('fixtures'),)
BOWER_COMPONENTS_ROOT = project_directory('bower')
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
