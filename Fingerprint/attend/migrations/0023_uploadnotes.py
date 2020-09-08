# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-05 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0022_posts_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(max_length=120, null=True)),
                ('Semister', models.CharField(max_length=120, null=True)),
                ('Field', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Sir', 'Sir')], max_length=120, null=True)),
                ('Subject', models.CharField(max_length=120, null=True)),
                ('FileNotes', models.CharField(max_length=120, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
