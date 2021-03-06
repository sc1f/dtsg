# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 22:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('statement', models.TextField()),
                ('platform', models.TextField()),
                ('image', models.FileField(upload_to='images/%Y/candidates/')),
                ('image_credit', models.CharField(max_length=200)),
                ('website', models.URLField()),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('winner', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Election')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Race'),
        ),
    ]
