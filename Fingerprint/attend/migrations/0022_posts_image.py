# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-04 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0021_auto_20180510_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
