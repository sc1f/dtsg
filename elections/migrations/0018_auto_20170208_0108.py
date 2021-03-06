# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0017_race_positions_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='votes_percentage',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='votes_received',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
