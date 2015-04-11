# -*- encoding: utf-8 -*-
import os
from PIL import Image
from cStringIO import StringIO

from django.db import models
from django.core.files.base import ContentFile

from apps.member.models import Member


class Album(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='投稿日時')
    title = models.CharField(max_length=200, blank=False, verbose_name='タイトル')
    author = models.ForeignKey(Member, blank=True, null=True, default=None)
    message = models.TextField(blank=False, verbose_name='本文')
    locked = models.BooleanField(default=False, verbose_name='ログインユーザーのみの閲覧')

    class Meta:
        verbose_name = verbose_name_plural = 'アルバム'

    def __unicode__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(Album)
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='投稿日時')
    title = models.CharField(max_length=200, blank=False, verbose_name='タイトル')
    author = models.ForeignKey(Member, related_name='author')
    message = models.TextField(blank=True, verbose_name='本文')
    image = models.ImageField(upload_to='photo', verbose_name='写真')
    thumb = models.ImageField(upload_to='photo', editable=False, verbose_name='サムネイル')

    class Meta:
        verbose_name = verbose_name_plural = '写真'

    def __unicode__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        self.compression = True
        super(Photo, self).__init__(*args, **kwargs)

    def filename(self, thumb=False):
        if thumb:
            return os.path.basename(self.thumb.name)
        else:
            return os.path.basename(self.image.name)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        root, ext = os.path.splitext(self.image.path)

        im = Image.open(StringIO(self.image.read()))

        y = im.size[0] > im.size[1]
        if y:
            l = im.size[0]
            s = im.size[1]
        else:
            s = im.size[0]
            l = im.size[1]

        new_size = 1920
        # 1920px以下 かつ 圧縮フラグがTrueでリサイズ
        if l > new_size and self.compression:
            a = new_size * s / l
            im.thumbnail(y and (new_size, a) or (a, new_size), Image.ANTIALIAS)

            fp = StringIO()
            im.save(fp, format=im.format)

            self.image.truncate(0)
            self.image.seek(0)
            self.image.write(fp.getvalue())

            fp.close()

        y = im.size[0] > im.size[1]
        if y:
            l = im.size[0]
            s = im.size[1]
        else:
            s = im.size[0]
            l = im.size[1]

        thumb_size = 200

        a = thumb_size * l / s
        thumb_image = im.resize(y and (a, thumb_size) or (thumb_size, a), Image.ANTIALIAS)

        tmp = StringIO()
        thumb_image.save(tmp, 'png')
        tmp.seek(0)
        tmp_file = ContentFile(tmp.read())

        self.thumb.save('%s-thumb%s' % (root, ext), tmp_file, save=False)

        r = super(Photo, self).save(force_insert, force_update, using, update_fields)
        return r


#pre_save.connect(pre_save_photo, sender=Photo)
