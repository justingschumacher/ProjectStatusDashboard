# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formEntry', '0016_auto_20171206_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='currentMilestone',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='previousMilestone',
            field=models.TextField(default='N/A', editable=False, help_text='Not Yet Implemented'),
        ),
        migrations.AddField(
            model_name='project',
            name='currentMilestone',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='previousMilestone',
            field=models.TextField(default='N/A', editable=False, help_text='Not Yet Implemented'),
        ),
    ]
