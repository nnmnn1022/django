# 운영 환경
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['52.79.97.19'] # 우리 도메인 또는 IP를 입력

DJANGO_APPS += [

]
PROJECT_APPS += [

]
THIRD_PARTY_APPS += [
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# 배포 시에는 STATICFILES_DIR 이 아닌 static root를 사용
STATIC_ROOT = BASE_DIR / 'static'