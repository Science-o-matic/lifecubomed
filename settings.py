# -*- coding: utf-8 -*-
import os
gettext = lambda s: s

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Martín Fuentes', 'fuentesmartin@gmail.com'),
    ('Antonio Barcia', 'antonio.barcia@gmail.com'),
    ('Javi Fuentes', 'jfuentess@gmail.com'),
)

MANAGERS = ADMINS

LANGUAGES = (
    ('es', gettext('Spanish')),
    ('en', gettext('English')),
    ('it', gettext('Italiano')),
    ('fr', gettext(u'Français')),
)

DEFAULT_LANGUAGE = 0

CMS_LANGUAGES = {
    1: [
        {
            'code': 'es',
            'name': gettext('Spanish'),
            'fallbacks': ['en'],
        },
        {
            'code': 'en',
            'name': gettext(u'English'),
        },
        {
            'code': 'it',
            'name': gettext(u'Italiano'),
            'public': False
        },
        {
            'code': 'fr',
            'name': gettext(u'Français'),
        },
        ],
    "default": {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': False
        }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'mycms.db'),
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

LOCALE_PATHS = (os.path.join(PROJECT_DIR, 'locale'),)

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/var/www/lifecubomed/media/'

STATIC_ROOT = '/var/www/lifecubomed/static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/"),
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = '0r6%7gip5tmez*vygfv+u14h@4lbt^8e2^26o#5_f_#b7%cm)u'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'accounts.middleware.RemoveNextMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

CMS_TEMPLATES = (
    ('home.html', gettext('Home Template')),
    ('page.html', gettext('Page Template')),
    ('new.html', gettext('New Template')),
    ('news.html', gettext('Cubomed News Template')),
    ('contact.html', gettext('Contact Template')),
    ('page2c.html', gettext('Page Template 2 colum')),
    ('page2.html', gettext('Page Template special')),
    ('page3c.html', gettext('Page template 3 colum')),
    ('page3cb.html', gettext('Page template 3 colum esp')),
    ('page3cnews.html', gettext('Page template 3 colum news')),
    ('sightings_page.html', gettext( 'Sightings Page Template')),
    ('registration/login.html', gettext('Accounts login template')),
    ('registration/registration_form.html', gettext('Accounts registration template')),
    ('sighting_report_form.html', gettext('Sight report template')),
)

CMS_PLACEHOLDER_CONF = {
    'new-image': {
        'plugins': ['PicturePlugin'],
        'name':gettext("Picture"),
    },
    'new-text': {
        'plugins': ['TextPlugin'],
        'name':gettext("Text and Link"),
    },
    'new-text-and-link': {
        'plugins': ['TextPlugin', 'LinkPlugin'],
        'name':gettext("New #2 Text"),
    },
}

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'cms',
    'menus',
    'mptt',
    'south',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'cms.plugins.inherit',
    'sekizai',
    'django_extensions',
    'cmsplugin_embeddedpages',
    'filer',
    'cmsplugin_contact',
    'imagestore',
    'sorl.thumbnail',
    'tagging',
    'imagestore.imagestore_cms',
    'tinymce',
    'cmsplugin_flickr_slideshow',
    'cmsplugin_gallery',
    'cmsplugin_youtube',
    'cms.plugins.flash',
    'accounts',
    'accounts.login',
    'accounts.register',
    'registration',
    'sightings',
    'sightings.report'
)

# Imagestore settings
IMAGESTORE_SHOW_USER = False

# Registration/auth settings
ACCOUNT_ACTIVATION_DAYS = 7

LOGFILE = os.path.join(PROJECT_DIR, "logfile.log")

try:
    from local_settings import *
except ImportError:
    pass

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE,
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
            }
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CMS_YOUTUBE_DEFAULT_AUTOPLAY = False
