# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formEntry', '0009_auto_20171113_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='goal',
            field=models.IntegerField(),
        ),
    ]
