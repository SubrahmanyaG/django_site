from __future__ import unicode_literals
import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

MEDIA_ROOT = 'user_details/static/'


class UserDetails(models.Model):
    person = models.OneToOneField(User)
    date_of_birth = models.DateField(null=True, blank=True)
    employee_id = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=MEDIA_ROOT, blank=True, null=True)
    # install Pillow to support
    current_address = models.CharField(max_length=127, null=True, blank=True)
    city = models.CharField(max_length=127, null=True, blank=True)
    state = models.CharField(max_length=127, null=True, blank=True)
    pin = models.CharField(max_length=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['person__username']

    def __unicode__(self):
        return "{}".format(self.person)


