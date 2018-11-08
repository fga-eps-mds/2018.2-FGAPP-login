from login.settings.common import *
from decouple import config

DEBUG = False
SECRET_KEY = config('SECRET_KEY', default='9_bjt+3r7c7&*^3)0jnga)b5f!8-)0+^j$bu-!bjlrcp2j$%(%')

ALLOWED_HOSTS = [config('HOST', default='*')]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='postgres'),
        'HOST': config('DB_HOST', default='db'), 
        'PORT': config('DB_PORT', default='5432'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASS', default='')
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'integraappfga@gmail.com'
EMAIL_HOST_PASSWORD = config('SECURITY_EMAIL_PASSWORD', default='passwordShouldBeIn.Env')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER