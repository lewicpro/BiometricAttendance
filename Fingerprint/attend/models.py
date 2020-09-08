# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
Mr='Mr'
Mrs='Mrs'
Ms='Ms'
Sir = 'Sir'
title=(
    (Mr ,'Mr'),
    (Mrs , 'Mrs'),
    (Ms , 'Ms'),
    (Sir , 'Sir')
)


CSE = 'CSE'
ECE = 'ECE'
ISNE = 'ISNE'
MECH = 'MECH'

CIVIL = 'CIVIL'
EDUCATION = 'EDUCATION'
department= (
    (CSE,'CSE'),
    (ECE, 'ECE'),
    (ISNE, 'ISNE'),
    (MECH, 'MECH'),
    (CIVIL, 'CIVIL'),
    (EDUCATION, 'EDUCATION')
)



class Register(models.Model):
    user = models.OneToOneField(User, null=True)
    Reg_number = models.CharField(max_length=120, blank=False, null=True)
    title = models.CharField(max_length=120, blank=False, choices=title, null=True)
    first_name = models.CharField(max_length=120, blank=False, null=True)
    second_name = models.CharField(max_length=120, blank=False, null=True)
    third_name = models.CharField(max_length=120, blank=True, null=True)
    depertment = models.CharField(max_length=120, choices=department, blank=False, null=True)
    subjects = models.CharField(max_length=120, blank=False, null=True)
    finger_print= models.CharField(max_length=300, blank=False, null=False)
    date_registered = models.DateField(auto_now_add=True, blank=False, null=True)
    phone_number = models.CharField(max_length=120, blank=False, null=True)
    position_type= models.CharField(max_length=120, blank=False, null=False)
    age = models.CharField(max_length=120, blank=False, null=True)
    email = models.EmailField(max_length=120, blank=False, null=True)



class RealAtendance(models.Model):
    user = models.CharField(max_length=120, blank=False, null=True)
    Reg_number = models.CharField(max_length=120, blank=False, null=True)
    title = models.CharField(max_length=120, blank=False, choices=title, null=True)
    first_name = models.CharField(max_length=120, blank=False, null=True)
    second_name = models.CharField(max_length=120, blank=False, null=True)
    third_name = models.CharField(max_length=120, blank=True, null=True)
    depertment = models.CharField(max_length=120, choices=department, blank=False, null=True)
    subjects = models.CharField(max_length=120, blank=False, null=True)
    finger_print= models.CharField(max_length=300, blank=True, null=True)
    date_registered = models.DateField(auto_now_add=True, blank=False, null=True)
    phone_number = models.CharField(max_length=120, blank=False, null=True)
    position_type= models.CharField(max_length=120, blank=False, null=False)
    age = models.CharField(max_length=120, blank=False, null=True)
    email = models.EmailField(max_length=120, blank=False, null=True)
    time = models.DateTimeField(auto_now=True, null=False)




class UploadNotes(models.Model):
    year = models.CharField(max_length=120, blank=True, null=True)
    semister = models.CharField(max_length=120, blank=True, null=True)
    field = models.CharField(max_length=120, blank=True, null=True)
    subject = models.CharField(max_length=120, blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    filenotes = models.FileField(blank=True, null=True)
    time = models.DateTimeField(auto_now=True, null=False)
    

class RealSignOut(models.Model):
    user = models.CharField(max_length=120, blank=False, null=True)
    Reg_number = models.CharField(max_length=120, blank=False, null=True)
    title = models.CharField(max_length=120, blank=False, choices=title, null=True)
    first_name = models.CharField(max_length=120, blank=False, null=True)
    second_name = models.CharField(max_length=120, blank=False, null=True)
    third_name = models.CharField(max_length=120, blank=True, null=True)
    depertment = models.CharField(max_length=120, choices=department, blank=False, null=True)
    subjects = models.CharField(max_length=120, blank=False, null=True)
    finger_print= models.CharField(max_length=300, blank=False, null=False)
    date_registered = models.DateField(auto_now_add=True, blank=False, null=True)
    phone_number = models.CharField(max_length=120, blank=False, null=True)
    position_type= models.CharField(max_length=120, blank=False, null=False)
    age = models.CharField(max_length=120, blank=False, null=True)
    email = models.EmailField(max_length=120, blank=False, null=True)
    time = models.DateTimeField(auto_now=True, null=False)


class Workers(models.Model):
    user = models.OneToOneField(User, null=True)
    title = models.CharField(max_length=120, blank=False, choices=title, null=True)
    first_name = models.CharField(max_length=120, blank=False, null=True)
    second_name = models.CharField(max_length=120, blank=False, null=True)
    third_name = models.CharField(max_length=120, blank=True, null=True)
    depertment = models.CharField(max_length=120, choices=department, blank=False, null=True)
    subjects = models.CharField(max_length=120, blank=False, null=True)
    date_registered = models.DateField(auto_now_add=True, blank=False, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    time_arrived= models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    phone_number = models.CharField(max_length=120, blank=False, null=True)
    email = models.EmailField(max_length=120, blank=False, null=True)
    def __str__(self):
        return str(self.user)
    @property
    def owner(self):
        return self.user



class Posts(models.Model):
    author_name =models.CharField(max_length=120, blank=False, null=True)
    description = models.TextField()
    image = models.FileField(null=True)
    comments = models.CharField(max_length=120, blank=False, null=True)
    # likes = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)

    def __str__(self):
        return str(self.author_name)

    def owner(self):
        return self.author_name


class suggestions(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    department = models.CharField(max_length=120, blank=False, null=False)
    suggest = models.CharField(max_length=120, blank=False, null=True)
    time = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return str(self.name)

    def owner(self):
        return self.name




class EventsDates(models.Model):
    Date = models.CharField(max_length=120, blank=False, null=True)
    Event = models.CharField(max_length=120, blank=False, null=True)
    Description = models.CharField(max_length=200, blank=False, null=True)
    def __str__(self):
        return str(self.Day)

    # def owner(self):
    #     return self.name


class SmsModel(models.Model):
    name = models.CharField(max_length=120, blank=False, null=True)
    phone = models.CharField(max_length=120, blank=False, null=True)


    def __str__(self):
        return str(self.name)

    def owner(self):
        return self.name