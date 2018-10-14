from login.settings.common import *

SECRET_KEY = '9_bjt+3r7c7&*^3)0jnga)b5f!8-)0+^j$bu-!bjlrcp2j$%(%'

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

