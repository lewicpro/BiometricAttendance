# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-04 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0003_auto_20180104_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='time_arrived',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]