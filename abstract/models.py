#-*- encoding: utf-8 -*-
from django.db import models
from django.utils import html
from django import forms

import markdown2

"""
messageのみを扱う
テキストのみの取得はstriptagで
markdownの変換は表示のタイミングでfilterを使う
"""
class MessageBase(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name="タイトル")
    message = models.TextField(blank=False, verbose_name="本文")
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="投稿日時")
    message_html = models.TextField(blank=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        md = markdown2.Markdown()
        encoded_html = md.convert(self.message)
        raw_text = html.strip_tags(encoded_html)
        self.raw_message = raw_text
        self.message_html = encoded_html
        return super(MessageBase, self).save(force_insert, force_update, using, update_fields)

    def message_stripped(self):
        return self.raw_message[0:40]

    @classmethod
    def exclude(cls):
        return 'message_html', 'message_stripped', 'raw_message',


