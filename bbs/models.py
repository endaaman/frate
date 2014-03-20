#-*- encoding: utf-8 -*-
from django.db import models
from django.utils import html
from django import forms
from abstract.models import MessageBase


class Thread(MessageBase):
    author = models.CharField(max_length=100, verbose_name="投稿者")
    locked = models.BooleanField(default=False, verbose_name="パスワードをかける")
    edit_key = models.CharField(max_length=10, verbose_name="編集キー")

    class Meta:
        verbose_name = verbose_name_plural = 'スレッド'

    def __unicode__(self):
        return self.title


class Comment(MessageBase):
    author = models.CharField(max_length=100, verbose_name="投稿者")
    edit_key = models.CharField(max_length=10, verbose_name="編集キー")
    thread = models.ForeignKey(Thread)

    class Meta:
        verbose_name = verbose_name_plural = 'コメント'

    def __unicode__(self):
        return self.message


