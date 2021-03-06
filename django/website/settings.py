#Django settings for  project.

# Build paths inside the project like this: path.join(BASE_DIR, ...)
from os import path
BASE_DIR = path.abspath(path.dirname(__file__))


########## DEFAULT DEBUG SETTINGS - OVERRIDE IN local_settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG
##########


########## DATABASES are configured in local_settings.py.*


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
import private_settings
SECRET_KEY = private_settings.SECRET_KEY

# http://psa.matiasaguirre.net/docs/backends/twitter.html
SOCIAL_AUTH_TWITTER_KEY = private_settings.SOCIAL_AUTH_TWITTER_KEY
SOCIAL_AUTH_TWITTER_SECRET = private_settings.SOCIAL_AUTH_TWITTER_SECRET

# http://psa.matiasaguirre.net/docs/backends/google.html#google-oauth2
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = private_settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = private_settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
########## END SECRET CONFIGURATION


########## MANAGER/EMAIL CONFIGURATION
# These email addresses will get all the error email for the production server
# (and any other servers with DEBUG = False )
ADMINS = (
    ('Sarah Bird', 'sarah@aptivate.org'),
    ('', ''),  # this is in case the above email doesn't work
)

MANAGERS = ADMINS

# these are the settings for production. We can override in the various
# local_settings if we want to
DEFAULT_FROM_EMAIL = 'sarah@aptivate.org'
SERVER_EMAIL = 'sarah@aptivate.org'
########## MANAGER/EMAIL CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Europe/London'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = path.join(BASE_DIR, 'uploads')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/opendatacomparison/uploads/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT= path.join(BASE_DIR, 'static')

# URL prefix for static files.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/opendatacomparison/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    path.join(BASE_DIR, 'media'),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'nested_inlines',
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'south',  # Database migration helpers
    'reversion',
    'floppyforms',
    'crispy_forms',
    'babel',
    'international',
    'widget_tweaks',
    'django_nose',
    'social.apps.django_app.default',
    'django_extensions',
    'rest_framework',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'homepage',
    'grid',
    'package',
    'core',
    'profiles',
    'publisher',
    'datamap',
    'downloads',
    'api',
)

########## END APP CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'reversion.middleware.RevisionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL Configuration
ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
# WSGI_APPLICATION = 'wsgi.application'
########## END URL Configuration


########## django-secure - intended for sites that use SSL
SECURE = False
if SECURE:
    INSTALLED_APPS += ("djangosecure", )

    # set this to 60 seconds and then to 518400 when you can prove it works
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_FRAME_DENY = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SECURE_SSL_REDIRECT = True
########## end django-secure


########## AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'social.backends.google.GoogleOAuth2',
    "django.contrib.auth.backends.ModelBackend",
    #"allauth.account.auth_backends.AuthenticationBackend",
)

# Some really nice defaults
#ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
########## END AUTHENTICATION CONFIGURATION


########## Custom user app defaults
# Select the correct user model
#AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "home"
########## END Custom user app defaults


########## SLUGLIFIER
#AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
########## END SLUGLIFIER

########## CRISPY
CRISPY_TEMPLATE_PACK = "bootstrap3"
########## END CRISPY

########## OPENCOMPARISON
LICENSES = ['MIT', 'BSD License']
########## END OPENCOMPARISON


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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
########## END LOGGING CONFIGURATION


########## BINDER STUFF
# Usually included by adding intranet_binder as a git submodule
# The name of the class to use to run the test suite
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

#MONKEY_PATCHES = ['intranet_binder.monkeypatches']
########## END BINDER STUFF

# this section allows us to do a deep update of dictionaries
import collections
from copy import deepcopy


def update_recursive(dest, source):
    for k, v in source.iteritems():
        if dest.get(k, None) and isinstance(v, collections.Mapping):
            update_recursive(dest[k], source[k])
        else:
            dest[k] = deepcopy(source[k])

# Define this here so it can be set by local_settings, or if not we set it later
ALLOWED_HOSTS = None

########## LOCAL_SETTINGS
# tasks.py expects to find local_settings.py so the database stuff is there
#--------------------------------
# local settings import
#from http://djangosnippets.org/snippets/1873/
#--------------------------------
try:
    import local_settings
except ImportError:
    print """
    -------------------------------------------------------------------------
    You need to create a local_settings.py file. Run ../../deploy/tasks.py
    deploy:<whatever> to use one of the local_settings.py.* files as your
    local_settings.py, and create the database and tables mentioned in it.
    -------------------------------------------------------------------------
    """
    import sys
    sys.exit(1)
else:
    # Import any symbols that begin with A-Z. Append to lists, or update
    # dictionaries for any symbols that begin with "EXTRA_".
    import re
    for attr in dir(local_settings):
        match = re.search('^EXTRA_(\w+)', attr)
        if match:
            name = match.group(1)
            value = getattr(local_settings, attr)
            try:
                original = globals()[name]
                if isinstance(original, collections.Mapping):
                    update_recursive(original, value)
                else:
                    original += value
            except KeyError:
                globals()[name] = value
        elif re.search('^[A-Z]', attr):
            globals()[attr] = getattr(local_settings, attr)

    CELERY_RESULT_BACKEND = "database"
    default_db = DATABASES['default']  # pyflakes: ignore
    CELERY_RESULT_DBURI = "mysql://{0}:{1}@{2}:{3}/{4}".format(
        default_db['USER'], default_db['PASSWORD'], default_db['HOST'],
        default_db['PORT'], default_db['NAME'])
########## END LOCAL_SETTINGS


##### from here on is stuff that depends on the value of DEBUG
##### which is set in LOCAL_SETTINGS


if DEBUG is False and ALLOWED_HOSTS is None:
    ########## SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    #ALLOWED_HOSTS = ["*"]
    ALLOWED_HOSTS = [
        '.',
        'www.',
        'fen-vz-ocds-stage.fen.aptivate.org',
        'ocds.open-contracting.org',
        'ocds.aptivate.org',
    ]
    ########## END SITE CONFIGURATION

########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    # Your stuff: custom template context processers go here
    'core.context_processors.core_values',
    'core.context_processors.current_path',
    'publisher.context_processors.publisher_headers',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)


# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    path.join(BASE_DIR, 'templates'),
)

if DEBUG:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
else:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
########## END TEMPLATE CONFIGURATION


########## Your stuff: Below this line define 3rd party libary settings
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + local_settings.EXTRA_INSTALLED_APPS

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    'PAGINATE_BY': 500,
    'MAX_PAGINATE_BY': 5000,
    'PAGINATE_BY_PARAM': 'page_size',
}

BOKEH_EMBED_JS_DIR = '/tmp/embed/js/'
