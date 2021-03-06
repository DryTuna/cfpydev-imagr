"""
Django settings for imagr_site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from configurations import Configuration, values

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Base(Configuration):
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True




    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '_0)ionh8p(-xw=uh-3_8un)^xo+=&obsad&lhohn-d93j(p!21'


    TEMPLATE_DEBUG = True

    TEMPLATE_DIRS = [os.path.dirname(__file__)+'/templates']

    ALLOWED_HOSTS = []

    AUTH_USER_MODEL = 'imagr_users.ImagrUser'


    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'sorl.thumbnail',
        'imagr_images',
        'registration',
    )

    # Application definition

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'imagr_site.urls'

    WSGI_APPLICATION = 'imagr_site.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.6/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'drytuna',
            'USER': 'drytuna',
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/

    STATIC_URL = '/static/'

    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

    MEDIA_URL = "/media/"

    AUTH_USER_MODEL = 'imagr_images.ImagrUser'

    THUMBNAIL_DEBUG = DEBUG

    ACCOUNT_ACTIVATION_DAYS = 2

class Dev(Base):
    pass


class Prod(Base):
    SECRET_KEY = values.SecretValue()
    DEBUG = False
