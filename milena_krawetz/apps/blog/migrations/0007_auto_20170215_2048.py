# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170215_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_active',
            new_name='is_published',
        ),
    ]
