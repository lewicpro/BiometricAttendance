# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-11 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0013_suggestions_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.IntegerField(null=True)),
                ('Month', models.IntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('Event', models.CharField(max_length=120, null=True)),
                ('Description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='posts',
            name='date',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='image',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='likes',
        ),
    ]
