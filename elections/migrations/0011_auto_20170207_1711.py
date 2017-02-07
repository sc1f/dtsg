# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0010_auto_20170207_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='election',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
