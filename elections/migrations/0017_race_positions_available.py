# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0016_auto_20170207_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='positions_available',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
