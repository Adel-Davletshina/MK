# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170215_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='blog/thumbnail/no-img.jpg', upload_to='/media/blog/thumbnail/'),
        ),
    ]
