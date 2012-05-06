# Django settings for cuba project.
import os
import sys
from config import config

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
  # ('Your Name', 'your_email@example.com'),
  ('Tyr Chen', 'tchen@tukeq.com')
  )

MANAGERS = ADMINS

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': 'cuba.db',                      # Or path to database file if using sqlite3.
    'USER': '',                      # Not used with sqlite3.
    'PASSWORD': '',                  # Not used with sqlite3.
    'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
  }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_HOME, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
  os.path.join(PROJECT_HOME, 'vendors'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
  )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a+$v8w!3*mn=sc7-he#-8r)@wcqcc&ms-@0zac!ag26)ca7*ol'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
  #     'django.template.loaders.eggs.Loader',
  )


# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
  "django.contrib.auth.context_processors.auth",
  "django.contrib.messages.context_processors.messages",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.static",
  "django.core.context_processors.media",
  "django.core.context_processors.request",
  )

MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  # Uncomment the next line for simple clickjacking protection:
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'debug_toolbar.middleware.DebugToolbarMiddleware',
  )

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
  # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
  # Always use forward slashes, even on Windows.
  # Don't forget to use absolute paths, not relative paths.
  os.path.join(PROJECT_HOME, 'templates'),
)

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  # Uncomment the next line to enable the admin:
  'django.contrib.admin',
  # Uncomment the next line to enable admin documentation:
  # 'django.contrib.admindocs',
  'django.contrib.comments',

  'cuba',

  # other modules
  'south',
  'bootstrap',            # for display
  'djangorestframework',  # for generating api
  'debug_toolbar',        # for debug purpose
)

AUTH_PROFILE_MODULE = 'cuba.UserProfile'

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_PANELS = (
  'debug_toolbar.panels.version.VersionDebugPanel',
  'debug_toolbar.panels.timer.TimerDebugPanel',
  'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
  'debug_toolbar.panels.headers.HeaderDebugPanel',
  'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
  'debug_toolbar.panels.template.TemplateDebugPanel',
  'debug_toolbar.panels.sql.SQLDebugPanel',
  'debug_toolbar.panels.signals.SignalDebugPanel',
  'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

USE_SOUTH = True

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'


# upyun related settings
USE_UPYUN = True
UPYUN_BINDING_DOMAIN = 'http://api-test.b0.upaiyun.com/'
UPYUN_API_DOMAIN = 'v0.api.upyun.com'
UPYUN_BUCKET = 'api-test'
UPYUN_USERNAME = 'tukeq'
UPYUN_PASSWORD = '1qaz2wsx'

IMG_CDN_DOMAIN = UPYUN_BINDING_DOMAIN


###############################################################
##                        Logging                            ##
###############################################################
LOG_PATH = os.path.join(os.getcwd(), config.get('logging', 'log_path'))
LOGGING_LEVEL = config.get('logging', 'log_level')

AUDIT_LOG_FILENAME = '%s/toureet-audit.log' % LOG_PATH
PROFILING_LOG_FILENAME = '%s/toureet-profiling.log' % LOG_PATH
MAIN_LOG_FILENAME = '%s/toureet-web.log' % LOG_PATH
LOST_LOG_FILENAME = '%s/toureet-lost.log' % LOG_PATH

LOG_BACKUP_COUNT = 50
LOG_MAX_BYTES = 5242880

LOGGING_CONFIG = 'django.utils.log.dictConfig'
LOGGING_HANDLER = 'cuba.utils.log.RotatingFileHandler'

if 'test' not in sys.argv:
  handler = ['console', 'main']
else:
  handler = ['main']

LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'formatters': {
    'verbose': {
      'format': '%(levelname)s %(asctime)s %(name)s %(processName)s[%(process)d] - %(message)s'
    },
    'simple': {
      'format': '%(levelname)s %(asctime)s %(message)s'
    },
    'audit': {
      'format': '%(asctime)s %(message)s'
    },
    'profiling': {
      'format': '%(asctime)s %(message)s'
    }

  },
  'filters': {

  },
  'handlers': {
    'null': {
      'level': 'DEBUG',
      'class': 'django.utils.log.NullHandler',
      },
    'console': {
      'level': LOGGING_LEVEL,
      'class': 'logging.StreamHandler',
      'formatter': 'simple'
    },
    'mail_admins': {
      'level': 'ERROR',
      'class': 'cuba.utils.admin_mail.AdminEmailHandler',
      'include_html': True,
      },
    'main': {
      'level': LOGGING_LEVEL,
      'class': LOGGING_HANDLER,
      'formatter': 'simple' if DEBUG else 'verbose',
      'filename': MAIN_LOG_FILENAME,
      'maxBytes': LOG_MAX_BYTES,
      'backupCount': LOG_BACKUP_COUNT

    },
    'audit': {
      'level': LOGGING_LEVEL,
      'class': LOGGING_HANDLER,
      'formatter': 'audit',
      'filename': AUDIT_LOG_FILENAME,
      #      'when': 'midnight',
      'maxBytes': LOG_MAX_BYTES,
      'backupCount': LOG_BACKUP_COUNT
    },
    'profiling': {
      'level': 'DEBUG',
      'class': LOGGING_HANDLER,
      'formatter': 'audit',
      'filename': PROFILING_LOG_FILENAME,
      #      'when': 'midnight',
      'maxBytes': LOG_MAX_BYTES,
      'backupCount': LOG_BACKUP_COUNT
    },
    'lost':{
      'level': 'DEBUG',
      'class': LOGGING_HANDLER,
      'formatter': 'audit',
      'filename': LOST_LOG_FILENAME,
      }
  },
  'loggers': {
    'django': {
      'handlers': ['null'],
      'propagate': True,
      'level': 'INFO',
      },
    'django.request': {
      'handlers': ['console'] if DEBUG else ['main', 'mail_admins'],
      'level': 'ERROR',
      'propagate': False,
      },
    '': {
      'handlers': handler if DEBUG else ['main', 'mail_admins'],
      'level': LOGGING_LEVEL,
      },
    'profiles.actions': {
      'handlers': ['audit'],
      'level': 'INFO',
      },
    'core.profiling': {
      'handlers': ['profiling'],
      'level': 'DEBUG',
      },
    'lost':{
      'handlers': ['lost'],
      'lever': 'DEBUG',
      }
  }
}