# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-12 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0015_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
