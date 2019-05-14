# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password','email','create_time']
    list_display_links = ['username']
    search_fields = ['username']
    list_filter = ['username']

admin.site.register(User, UserAdmin)
class FileAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'file_size','file','create_time']
    list_display_links = ['file_name']
    search_fields = ['file_name']
admin.site.register(File,FileAdmin)