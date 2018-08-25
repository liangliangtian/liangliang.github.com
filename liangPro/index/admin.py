# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password','email','create_time']
    #添加链接
    list_display_links = ['username']
    #添加可编辑字段
    #list_editable = ['address', 'city']
    #添加搜索框
    search_fields = ['username']
    #date_hierarchy = DateField
    #右面添加过滤器
    list_filter = ['username']

admin.site.register(User, UserAdmin)
class FileAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'file_size','file','create_time']
    #添加链接
    list_display_links = ['file_name']
    #添加可编辑字段
    #list_editable = ['address', 'city']
    #添加搜索框
    search_fields = ['file_name']

admin.site.register(File,FileAdmin)