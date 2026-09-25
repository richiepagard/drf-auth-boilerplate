from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dxb@%f)%+^12eor+mnviru6!5c+c6c3utlrb-#7&rwsv^-w$x@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


### Apps settings config ###
from .configs import INSTALLED_APPS

### Middleware config ###
from .configs import MIDDLEWARE

### Templates config ###
from .configs import TEMPLATES

### Databases config ###
from .configs import DATABASES

### Passwords auth validators config ###
from .configs import AUTH_PASSWORD_VALIDATORS


# WSGI & ROOT ENDPOINTS
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


### Default user model ###
AUTH_USER_MODEL = "accounts.User"


### Rest framework config ###
from .configs import REST_FRAMEWORK

### Simple JWT configs ###
from .configs import SIMPLE_JWT

### DRF spectacular configs ###
from .configs import SPECTACULAR_SETTINGS
