# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-25 06:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='pictures/%Y/%m', verbose_name='画')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('zan_nums', models.IntegerField(default=0, verbose_name='点赞人数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '画展',
                'verbose_name': '画展',
            },
        ),
    ]
