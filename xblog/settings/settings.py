# -*- coding: utf-8 -*-

"""
Django settings for xblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ['XBLOG_SECRET_KEY']


SECRET_KEY = 'weojktk+2z-ip=0wk1=q%06n^h_5l&wqy3_$&2+ojn(@2_gh*4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.xus.io']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_markdown',
    'adminfiles',
    'sorl.thumbnail',
    'haystack',
    'apps.blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

ROOT_URLCONF = 'xblog.urls'

WSGI_APPLICATION = 'xblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': os.path.join(BASE_DIR, 'db.mysql'),
    #}

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xblog',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/data/static/'

MEDIA_URL = '/media/' 
MEDIA_ROOT = '/data/media/' 


JQUERY_URL = 'js/jquery.min.js'

MARKDOWN_EXTENSIONS = ['extra', 'codehilite']

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 6

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = 'DENY'



