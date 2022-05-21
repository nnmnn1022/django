# 작업하는 환경
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DJANGO_APPS += [

]
PROJECT_APPS += [

]
THIRD_PARTY_APPS += [
    'debug_toolbar',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

