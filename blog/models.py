#-*- encoding: utf-8 -*-
from django.db import models
from django import forms
from abstract.models import MessageBase


class Blog(MessageBase):
    author = models.ForeignKey('member.Member', verbose_name='投稿者')
    url_name = models.CharField(max_length=100, verbose_name='名前')

    class Meta:
        verbose_name = verbose_name_plural = 'ブログ'

    def __unicode__(self):
        return self.title


class Comment(MessageBase):
    blog = models.ForeignKey(Blog)
    author = models.CharField(max_length=100, blank=False, verbose_name='投稿者')
    edit_key = models.CharField(max_length=10, verbose_name="編集キー")

    class Meta:
        verbose_name = verbose_name_plural = 'コメント'

    def __unicode__(self):
        return self.title


