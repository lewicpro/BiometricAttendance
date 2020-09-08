# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-07 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0018_register_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealAtendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120, null=True)),
                ('Reg_number', models.CharField(max_length=120, null=True)),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Sir', 'Sir')], max_length=120, null=True)),
                ('first_name', models.CharField(max_length=120, null=True)),
                ('second_name', models.CharField(max_length=120, null=True)),
                ('third_name', models.CharField(blank=True, max_length=120, null=True)),
                ('depertment', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL'), ('EDUCATION', 'EDUCATION')], max_length=120, null=True)),
                ('subjects', models.CharField(max_length=120, null=True)),
                ('finger_print', models.CharField(max_length=300)),
                ('date_registered', models.DateField(auto_now_add=True, null=True)),
                ('phone_number', models.CharField(max_length=120, null=True)),
                ('position_type', models.CharField(max_length=120)),
                ('age', models.CharField(max_length=120, null=True)),
                ('email', models.EmailField(max_length=120, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='register',
            name='Reg_number',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
