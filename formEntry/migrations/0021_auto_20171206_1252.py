# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formEntry', '0020_auto_20171206_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='goalType',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='goalType',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
