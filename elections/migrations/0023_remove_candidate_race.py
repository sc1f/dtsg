# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 20:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0022_auto_20170209_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='race',
        ),
    ]
