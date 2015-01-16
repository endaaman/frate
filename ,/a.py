#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frate.settings")



import datetime 
import time
from django.utils.timezone import utc
from bbs.models import *

tt = Thread.objects.all()
for t in tt:
    t.last_update = t.pub_date
    t.save()