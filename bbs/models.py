#-*- encoding: utf-8 -*-
from django.db import models
from django.utils import html
from django import forms

import datetime
from django.utils.timezone import utc


class Thread(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="投稿日時")
    title = models.CharField(max_length=200, blank=False, verbose_name="タイトル")
    author = models.CharField(max_length=100, verbose_name="投稿者")
    message = models.TextField(blank=False, verbose_name="本文")
    locked = models.BooleanField(default=False, verbose_name="パスワードをかける")
    edit_key = models.CharField(max_length=10, verbose_name="編集キー")
    last_update = models.DateTimeField(editable=False, verbose_name="最終更新日時")

    class Meta:
        verbose_name = verbose_name_plural = 'スレッド'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # self.last_update = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Thread, self).save(*args, **kwargs)


    @property
    def is_new(self):
        limit = datetime.datetime.utcnow().replace(tzinfo=utc) - datetime.timedelta(days=3)
        return self.last_update > limit


class Comment(models.Model):
    thread = models.ForeignKey(Thread)
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="投稿日時")
    author = models.CharField(max_length=100, verbose_name="投稿者")
    message = models.TextField(blank=False, verbose_name="本文")
    edit_key = models.CharField(max_length=10, verbose_name="編集キー")


    class Meta:
        verbose_name = verbose_name_plural = 'コメント'

    def __unicode__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.thread.save()
        super(Comment, self).save(*args, **kwargs)
