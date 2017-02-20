# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0013_election_election_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('position_name', models.CharField(max_length=200)),
                ('positions_available', models.PositiveSmallIntegerField()),
                ('position_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Election')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Race')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Position'),
            preserve_default=False,
        ),
    ]
