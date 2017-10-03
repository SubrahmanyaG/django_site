# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-03 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='city',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='current_address',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='employee_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='pin',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='state',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
    ]