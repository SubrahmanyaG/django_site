# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-03 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0002_auto_20171003_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='/home/hi-325/workspace/djangoAssignment/django_site/media/'),
        ),
    ]