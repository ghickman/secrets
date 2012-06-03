# Django settings for secrets project.
import os

import dj_database_url


DIRNAME = os.path.abspath(os.path.dirname(__file__))

DEBUG = bool(os.environ.get('DEBUG', False))

ADMINS = (('George Hickman', 'george@ghickman.co.uk'),)
MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost/secrets')
}

TIME_ZONE = 'Europe/London'
USE_TZ = True

LANGUAGE_CODE = 'en-gb'
USE_I18N = True  # Internationalization
USE_L10N = True  # Locale

# S3 Backend
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# Static
MEDIA_ROOT = 'client_media'
MEDIA_URL = '/media/'
STATIC_ROOT = 'static_media'
STATIC_URL = 'http://{0}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
STATICFILES_DIRS = (os.path.join(DIRNAME, 'static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

TEMPLATE_DIRS = (os.path.join(DIRNAME, 'templates'))
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'secrets.urls'
SECRET_KEY = 'pl#%lb5=ws784n%ioe@+1f*s_1**e#g4f225*pr0&hjll6kw%q'
SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'core',

    'django_simple_aes_field',
    'storages',
    'tastypie',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

