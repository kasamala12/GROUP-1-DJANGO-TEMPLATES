"""
Django settings for news_portal project.

GROUP 1: DJANGO TEMPLATES
University News Portal — built to demonstrate:
 - What Django Templates are
 - Django Template Language (DTL)
 - Template directories and configuration
 - Rendering templates using the render() function
 - Passing data from views to templates
 - Displaying variables
 - Comments in templates
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-demo-key-for-university-news-portal'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Our app
    'news',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'news_portal.urls'

# --- TEMPLATE CONFIGURATION ---------------------------------------------
# 'DIRS' can point to a project-level templates folder, and
# 'APP_DIRS': True tells Django to also look inside each app's own
# "templates/" directory (news/templates/news/...). This is exactly the
# "template directories and configuration" topic for this group.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'news_portal.wsgi.application'

# Database is optional for this project — news data is stored in a
# Python list of dictionaries in news/data.py instead of a real DB.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'news' / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
