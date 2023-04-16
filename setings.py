# settings.py
import os
import sys

from allauth import socialaccount
from django.conf import settings
import allauth.socialaccount
import allauth.socialaccount.models
from allauth.socialaccount.providers import google
from allauth.socialaccount.providers.twitter import views as twitter_views
from allauth.socialaccount.providers.facebook import views as facebook_views
from allauth.socialaccount.providers import linkedin
from allauth.account.auth_backends import AuthenticationBackend
from django.contrib import staticfiles
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import accounts, art_event, helpy, offer, reviews, telegram_bot
from helpy import my_menu, static

SECRET_KEY = 'django-insecure-!*_55!=_67w%7*s)(3=#2l)h0)+7!jw^y3v2dp^9^co1*sp%gx'
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
STATIC_ROOT = os.path.join( BASE_DIR, 'staticfiles' )
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join( BASE_DIR, 'static' ),
    os.path.join( BASE_DIR, 'helpy', 'static', 'helpy' ),
]
WSGI_APPLICATION = 'helpy.wsgi.application'

# получаем путь к виртуальной среде VIRTUAL_ENV = os.environ.get('VIRTUAL_ENV') BASE_DIR / "static",
VIRTUAL_ENV = os.getenv( 'VIRTUAL_ENV' )
if VIRTUAL_ENV:
    VENV_PATH = os.path.join( VIRTUAL_ENV, 'Lib', 'site-packages' )
    if os.path.exists( VENV_PATH ):
        sys.path.insert( 0, VENV_PATH )
INSTALLED_APPS = [
    'django.template',
    'django.contrib.admin',
    'django_countries',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.sites',
    'django-bootstrap4',
    'django_telegram_bot',
    'telegram_bot',
    'telegram_bot.bot',
    'crispy_forms',
    'widget_tweaks',
    'accounts'
    'art_event',
    'helpy',
    'offer',
    'reviews',
    'telegram_bot',
    'my_menu'
    'allauth',
    'allauth.account',
    'django.contrib.staticfiles',
    'allauth.socialaccount',
    'socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.linkedin',
]
# Указываем доступные языки для нашего проекта.
LANGUAGES = [
    ('uk', 'Українська'),
    ('th', 'ภาษาไทย'),
    ('en', 'English'),
    ('fr', 'Français'),
    ('it', 'Italiano'),
    ('de', 'Deutsch'),
    ('ru', 'Русский'),
]
ROOT_URLCONF = 'djangoProject.urls'
MEDIA_URL = '/media/'
SITE_URL = 'http://127.0.0.1:8000/'
MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOCALE_PATHS = [
    os.path.join( BASE_DIR, 'locale' ),
]
# Settings for django-bootstrap4
# Определяем переменную BOOTSTRAP4_FOLDER
BOOTSTRAP4_FOLDER = os.path.abspath( os.path.join( BASE_DIR, "static", "bootstrap4" ) )
# Проверяем, есть ли BOOTSTRAP4_FOLDER в переменной sys.path
if BOOTSTRAP4_FOLDER not in sys.path:
    # Если нет, то добавляем BOOTSTRAP4_FOLDER в начало списка sys.path
    sys.path.insert( 0, BOOTSTRAP4_FOLDER )
BOOTSTRAP4 = {
    "error_css_class": "bootstrap4-error",
    "required_css_class": "bootstrap4-required",
    "javascript_in_head": True,
    "include_jquery": True,
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join( BASE_DIR, 'templates/helpy' ),
            os.path.join( BASE_DIR, 'templates/accounts' ),
            os.path.join( BASE_DIR, 'helpy/templatetags' )
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'helpy.context_processors.footer_context',
                'django.template.context_processors.request',
                'helpy.context_processors.languages_flags.languages_with_flags',
                'helpy.context_processors.menu_items',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.csrf',
                'allauth.account.context_processors.helpy',
                'allauth.socialaccount.context_processors.socialaccount',
            ],
        },
    },
]
# Добавляем поддержку переводов.
USE_I18N = True
# Задаем язык по умолчанию.
LANGUAGE_CODE = 'en-us'

MIDDLEWARE = [
    # ...
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]
# Добавляем поддержку временных зон.
USE_TZ = True

# Добавляем поддержку форматирования дат и времени.
USE_L10N = True

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 5,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LOGIN_REDIRECT_URL = '/'
AUTHENTICATION_BACKENDS = [
    # ...
    'allauth.account.auth_backends.AuthenticationBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
    # ... 'allauth.socialaccount.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': 'your-client-id-here',
            'secret': 'your-secret-key-here',
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False
    },
    # ...Facebook, Twitter, Google
}
SOCIALACCOUNT_ADAPTER = 'accounts.adapters.CustomSocialAccountAdapter'
AUTH_USER_MODEL = 'accounts.Visitor'