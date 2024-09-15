import os
from pathlib import Path
from environ import Env
env=Env()
Env.read_env()

ENVIRONMENT = env('ENVIRONMENT',default="production")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [".replit.dev", ".replit.app","*"]
CSRF_TRUSTED_ORIGINS = ["https://*.replit.dev", "https://*.replit.app"]

INSTALLED_APPS = [
  'jazzmin',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.sites',
  'allauth',
  'allauth.account',
  'allauth.socialaccount',
  'import_export',
  'cloudinary_storage',
  'cloudinary',
  'crispy_forms',
  'crispy_bootstrap5',
  'app'
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'allauth.account.middleware.AccountMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR/'templates'],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]


WSGI_APPLICATION = 'src.wsgi.application'

import dj_database_url

if ENVIRONMENT == 'development':
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': BASE_DIR / 'db.sqlite3',
    }
  }
else:
  DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
  }

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
  },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'

if ENVIRONMENT == 'development':
  MEDIA_ROOT = BASE_DIR / 'media' 
else:
  DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
  CLOUDINARY_STORAGE={
      'CLOUDINARY_URL': env('CLOUDINARY_URL')
  }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
  'site_title': '毛毛與秀秀的資料庫',
  'site_header': 'Hello World',
  'site_brand': 'I am brand',
  'welcome_sign': '歡迎來到毛毛與秀秀的資料庫',
  'copyright': 'ryowuandjanet.com',
}

AUTHENTICATION_BACKENDS = [
  'django.contrib.auth.backends.ModelBackend',
  'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID=1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER=env('EMAIL_ADDRESS')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_PORT=587
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=f"Django App Name {env('EMAIL_ADDRESS')}"
ACCOUNT_EMAIL_SUBJECT_PREFIX=''

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'home'
# ACCOUNT_AUTHENTICATED_METHOD = 'username_email'
# ACCOUNT_EMAIL_REQUIRED = True

# ACCOUNT_UNIQUE_EMAIL = True

# ACCOUNT_EMAIL_VERIFICATION  = 'mandatory'
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7

from import_export.formats.base_formats import XLSX, CSV,JSON
EXPORT_FORMATS = [XLSX, CSV,JSON]
IMPORT_FORMATS = [XLSX, CSV,JSON]


