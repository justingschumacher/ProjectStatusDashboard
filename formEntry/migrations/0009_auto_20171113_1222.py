# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formEntry', '0008_project_revisedduedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='comments',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='executiveSummary',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]