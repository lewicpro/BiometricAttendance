# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-09 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0012_suggestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestions',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
