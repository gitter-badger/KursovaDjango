import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '!#_rtp48og7bg%n)n(vvs*@)iqu-&c&08+@k_+=yem(94#sl7j'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Kursova.urls'

WSGI_APPLICATION = 'Kursova.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'containers.db')
    }
}

LANGUAGE_CODE = 'uk-ua'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "media"),
    os.path.join(BASE_DIR, "static"),
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

STATIC_URL = '/static/'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)