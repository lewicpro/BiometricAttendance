# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display =[
        'pk',
    # 'user',
    'title',
    'first_name',
    'second_name',
    'third_name',
    'depertment',
    'subjects',
    'date_registered',
    'finger_print',
    'phone_number',
    'email'
    # '__all__'
    ]


class WorkersAdmin(admin.ModelAdmin):
    list_display =[
    'user',
    'title',
    'first_name',
    'second_name',
    'third_name',
    'depertment',
    'subjects',
    'date_registered',
    'time_arrived',
    'time_arrived',
    'percentage',
    'email'
    ]

class PostsAdmin(admin.ModelAdmin):
    list_display =[
    'author_name',
    'description',
    'image',
    'comments',
    # 'likes',
    # 'date',
    ]


class UploadNotesAdmin(admin.ModelAdmin):
    list_display =[
    'year',
    'semister',
    'field',
    'subject',
    'title',
    'filenotes',
    'time',
    ]


class SmsAdmin(admin.ModelAdmin):
    list_display =[
        'name',
        'phone',
    ]













class DescAdmin(admin.ModelAdmin):
    list_display =[
    'name',
    'department',
    'suggest',
    'time',
    ]



class EventsAdmin(admin.ModelAdmin):
    list_display =[
    'Date',
    'Event',
    'Description',
    ]




class RealAtendanceAdmin(admin.ModelAdmin):
    list_display =[
    'Reg_number',
    'first_name',
    'second_name',
    'third_name',
    'depertment',
    'subjects',
    'finger_print',
    'date_registered',
    'phone_number',
    'time',
    ]



class RealSignOutAdmin(admin.ModelAdmin):
    list_display =[
    'user',
    'Reg_number',
    'first_name',
    'second_name',
    'third_name',
    'depertment',
    'subjects',
    'finger_print',
    'date_registered',
    'phone_number',
    'time',
    ]





admin.site.register(Workers, WorkersAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(suggestions, DescAdmin)
admin.site.register(Register, RegisterAdmin)
admin.site.register(EventsDates, EventsAdmin)
admin.site.register(RealAtendance, RealAtendanceAdmin)
admin.site.register(RealSignOut, RealSignOutAdmin)
admin.site.register(UploadNotes, UploadNotesAdmin)
admin.site.register(SmsModel, SmsAdmin)