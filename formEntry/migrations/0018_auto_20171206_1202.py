# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formEntry', '0017_auto_20171206_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='inputGoals',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='outputGoals',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='inputGoals',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='outputGoals',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
