#-*- encoding: utf-8 -*-
from django.db import models
from django import forms


class Blog(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="投稿日時")
    title = models.CharField(max_length=200, blank=False, verbose_name="タイトル")
    author = models.ForeignKey('member.Member', verbose_name='投稿者')
    message = models.TextField(blank=False, verbose_name="本文")
    url_name = models.CharField(max_length=100, verbose_name='名前')

    class Meta:
        verbose_name = verbose_name_plural = 'ブログ'

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    author = models.CharField(max_length=100, blank=False, verbose_name='投稿者')
    message = models.TextField(blank=False, verbose_name="本文")
    edit_key = models.CharField(max_length=10, verbose_name="編集キー")

    class Meta:
        verbose_name = verbose_name_plural = 'コメント'

    def __unicode__(self):
        return self.title


