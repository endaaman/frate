# -*- coding: utf-8 -*-

import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.core.files.storage import FileSystemStorage
from django_thumbs.db.models import ImageWithThumbsField

# print '%s年%s月%s日\n' % (d.year, d.month, d.day)

MED_START = 1918

fs = FileSystemStorage()


class Member(models.Model):
    name = models.CharField(max_length=100)
    entrance = models.IntegerField()
    remaining = models.IntegerField(default=0, null=True)
    description = models.TextField(default='', blank=True)
    join_year = models.IntegerField(default=0, null=True)
    grade = models.IntegerField(default=0, null=True)
    image = ImageWithThumbsField(upload_to='photo', storage=fs, default='', null=True, blank=True, sizes=((200, 200),) )

    class Meta:
        verbose_name = verbose_name_plural = 'メンバー'
        # ordering = ['belonging_for', '-grade']

    def __unicode__(self):
        return self.name

    def name_entrance(self):
        return '%s %s' % (self.name, self.entrance)

    def grade(self):
        # print('%d年入学 %d期 %d留 %d年目 %d年生' % (nyugaku, enter, ryunen, nenme, nenme - ryunen))
        d = datetime.datetime.today()
        return d.year - self.entrance - MED_START - self.remaining + ( 1 if d.month > 3 else 0 )

    def belonging_for(self):
        d = datetime.datetime.today()
        return d.year - self.join_year + ( 1 if d.month > 3 else 0 )


def pre_save_member(sender, instance, **kwargs):
    if (instance.join_year is None) or (instance.join_year is 0 ):
        instance.join_year = instance.entrance + MED_START


pre_save.connect(pre_save_member, sender=Member)
