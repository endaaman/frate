# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x8a\x95\xe7\xa8\xbf\xe6\x97\xa5\xe6\x99\x82')),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe3\x82\xbf\xe3\x82\xa4\xe3\x83\x88\xe3\x83\xab')),
                ('message', models.TextField(verbose_name=b'\xe6\x9c\xac\xe6\x96\x87')),
                ('locked', models.BooleanField(default=False, verbose_name=b'\xe3\x83\xad\xe3\x82\xb0\xe3\x82\xa4\xe3\x83\xb3\xe3\x83\xa6\xe3\x83\xbc\xe3\x82\xb6\xe3\x83\xbc\xe3\x81\xae\xe3\x81\xbf\xe3\x81\xae\xe9\x96\xb2\xe8\xa6\xa7')),
                ('author', models.ForeignKey(default=None, blank=True, to='member.Member', null=True)),
            ],
            options={
                'verbose_name': '\u30a2\u30eb\u30d0\u30e0',
                'verbose_name_plural': '\u30a2\u30eb\u30d0\u30e0',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x8a\x95\xe7\xa8\xbf\xe6\x97\xa5\xe6\x99\x82')),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe3\x82\xbf\xe3\x82\xa4\xe3\x83\x88\xe3\x83\xab')),
                ('message', models.TextField(verbose_name=b'\xe6\x9c\xac\xe6\x96\x87', blank=True)),
                ('image', models.ImageField(upload_to=b'photo', verbose_name=b'\xe5\x86\x99\xe7\x9c\x9f')),
                ('thumb', models.ImageField(verbose_name=b'\xe3\x82\xb5\xe3\x83\xa0\xe3\x83\x8d\xe3\x82\xa4\xe3\x83\xab', editable=False, upload_to=b'photo')),
                ('album', models.ForeignKey(to='photo.Album')),
                ('author', models.ForeignKey(related_name='author', to='member.Member')),
                ('member', models.ManyToManyField(related_name='member', to='member.Member', blank=True)),
            ],
            options={
                'verbose_name': '\u5199\u771f',
                'verbose_name_plural': '\u5199\u771f',
            },
            bases=(models.Model,),
        ),
    ]
