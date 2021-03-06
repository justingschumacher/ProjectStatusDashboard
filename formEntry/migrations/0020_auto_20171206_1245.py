# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formEntry', '0019_auto_20171206_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='comments',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='definition',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='executiveSummary',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='inputGoals',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='outputGoals',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='pathToGreen',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='comments',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='definition',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='executiveSummary',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='inputGoals',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='outputGoals',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='pathToGreen',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
    ]
