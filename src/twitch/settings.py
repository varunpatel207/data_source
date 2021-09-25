import os

# YAML configurations
import yaml

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 'src1' is BASE_DIR

# 'src1/config/config.yml'
CONFIG_FILE = os.path.join(BASE_DIR, '../', 'config', 'config.yml')

# config_data will contain configuration details like credentials, API Keys, Secret Keys
with open(CONFIG_FILE) as f:
    config_data = yaml.safe_load(f)

COINMARKETCAP_API_URL = config_data['COINMARKETCAP']['API_URL']
COINMARKETCAP_API_KEY = config_data['COINMARKETCAP']['API_KEY']

COINGECKO_API_URL = config_data['COINGECKO']['API_URL']
COINGECKO_API_KEY = config_data['COINGECKO']['API_KEY']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config_data['SECRET_KEY']
CONFIG = config_data

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

BASE_URL = config_data.get('BASE_URL')
# Application definition


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps',
]


MIDDLEWARE = [
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CSRF_COOKIE_SECURE = True

ROOT_URLCONF = 'twitch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'lstrip_blocks': True,
           'trim_blocks': True, 'environment': 'apps.jinja2.environment',
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        }
    },
]

WSGI_APPLICATION = 'twitch.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config_data['DB']['NAME'],
        'USER': config_data['DB']['USER'],
        'PASSWORD': config_data['DB']['PASSWORD'],
        'HOST': config_data['DB']['HOST'],
        'PORT': config_data['DB']['PORT'],
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-IN'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_BROWSER_XSS_FILTER = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'apps', 'static', 'apps'),
]

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL of uploaded media files
MEDIA_URL = '/media/'

# Where media files will be stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SESSION_ENGINE = 'django.contrib.sessions.backends.file'

