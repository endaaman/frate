#-*- encoding: utf-8 -*-
from django.db import models
from django.utils import html
from django import forms
from abstract.models import MessageBase


class Thread(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="投稿日時")
    title = models.CharField(max_length=200, blank=False, verbose_name="タイトル")
    author = models.CharField(max_length=100, verbose_name="投稿者")
    message = models.TextField(blank=False, verbose_name="本文")
    locked = models.BooleanField(default=False, verbose_name="パスワードをかける")
    edit_key = models.CharField(max_length=10, verbose_name="編集キー")

    class Meta:
        verbose_name = verbose_name_plural = 'スレッド'

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    thread = models.ForeignKey(Thread)
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="投稿日時")
    author = models.CharField(max_length=100, verbose_name="投稿者")
    message = models.TextField(blank=False, verbose_name="本文")
    locked = models.BooleanField(default=False, verbose_name="パスワードをかける")
    edit_key = models.CharField(max_length=10, verbose_name="編集キー")


    class Meta:
        verbose_name = verbose_name_plural = 'コメント'

    def __unicode__(self):
        return self.message


