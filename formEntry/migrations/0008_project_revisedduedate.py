# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formEntry', '0007_project_projectstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='revisedDueDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
