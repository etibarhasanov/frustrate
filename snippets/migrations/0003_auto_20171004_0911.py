# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_statistics_averageholdingduration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='nps',
            field=models.IntegerField(),
        ),
    ]