# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formEntry', '0005_auto_20171106_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectRecordID',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Number: '),
        ),
    ]