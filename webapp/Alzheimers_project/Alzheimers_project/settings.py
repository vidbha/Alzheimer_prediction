"""
Django settings for Alzheimers_project project.
"""

from pathlib import Path
import os # DEPLOYMENT: Import the 'os' module to access environment variables

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# DEPLOYMENT: Load the SECRET_KEY from an environment variable for security.
# On Render, you will set this in the "Environment" section.
SECRET_KEY = os.environ.get('SECRET_KEY', 'a-default-fallback-key-for-local-use')

# DEPLOYMENT: DEBUG must be False in production.
# Render automatically sets an environment variable IS_RENDER to "true".
# We use this to keep DEBUG=True locally and set it to False when deployed.
DEBUG = os.environ.get('RENDER', False) != 'true'

# DEPLOYMENT: Add your app's URL when you deploy.
# The wildcard '*' is a simple starting point, but it's more secure to be specific.
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # DEPLOYMENT: Add whitenoise for serving static files
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    "Alzheimers_detection",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # DEPLOYMENT: Add whitenoise middleware right after SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Alzheimers_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Alzheimers_project.wsgi.application'


# Database
# The default SQLite database is fine for a simple, free-tier app on Render.
# For larger apps, you would switch to PostgreSQL.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# DEPLOYMENT: Add settings for serving static files in production.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'