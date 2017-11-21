# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formEntry', '0002_auto_20171105_2055'),
    ]

    operations = [
        migrations.DeleteModel(
            name='formAdmin',
        ),
        migrations.AlterField(
            model_name='project',
            name='completionDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='createdDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='didNotMeetDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
