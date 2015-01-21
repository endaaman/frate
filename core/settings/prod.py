# -*- coding: utf-8 -*-

from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'prod.sqlite3'),
    }
}

ALLOWED_HOSTS = ['*']

try:
    from local import *
except:
    pass
