# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 100)
	email = models.EmailField(blank=True)
	create_time = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.username
	class Meta:
		verbose_name = '用户'
		verbose_name_plural = verbose_name
		ordering = ['create_time']
class File(models.Model):
  
    file_name=models.CharField(max_length=20)
    file_size=models.IntegerField()
    create_time=models.DateTimeField(auto_now_add=True)
    file=models.ImageField(upload_to='static/upload')
    user=models.ForeignKey(User)

    def __str__(self):
        return self.file_name
    class Meta:
        verbose_name='视频'
        verbose_name_plural=verbose_name