#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from cStringIO import StringIO


im = Image.open('big.jpg')
fp = StringIO()
im.save(fp, format=im.format)
f = open('a.jpg', 'w+b')
f.write(fp.getvalue())
fp.close()
f.close()

print im.format