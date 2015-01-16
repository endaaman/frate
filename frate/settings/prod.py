# -*- coding: utf-8 -*-

from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

try:
    from local import *
except:
    pass
