# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-13 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0016_workers_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
