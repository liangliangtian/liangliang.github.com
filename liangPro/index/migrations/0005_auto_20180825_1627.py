# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-25 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20180824_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(upload_to='static/upload'),
        ),
    ]