# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/%Y/candidates/'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='image_credit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
