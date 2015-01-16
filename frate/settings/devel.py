# -*- coding: utf-8 -*-

from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

INSTALLED_APPS += (
    'devserver',
)

try:
    from local import *
except:
    pass
