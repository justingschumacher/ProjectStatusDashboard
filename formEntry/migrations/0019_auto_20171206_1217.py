# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formEntry', '0018_auto_20171206_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='previousMilestone',
            field=models.TextField(default='N/A', help_text='Not Yet Implemented'),
        ),
        migrations.AlterField(
            model_name='project',
            name='previousMilestone',
            field=models.TextField(default='N/A', help_text='Not Yet Implemented'),
        ),
    ]