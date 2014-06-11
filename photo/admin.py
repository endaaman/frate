from django.contrib import admin

# Register your models here.

from models import *
from django.contrib import admin
admin.site.register(Photo)
admin.site.register(Album)
admin.site.register(Hero)
