# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-04 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0006_auto_20180104_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='user',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
