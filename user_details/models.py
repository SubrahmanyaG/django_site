from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    person = models.OneToOneField(User)
    date_of_birth = models.DateField(null=True, blank=True)
    employee_id = models.IntegerField(null=True, blank=True)
    image = models.FileField(blank=True, null=True)
    current_address = models.CharField(max_length=127, null=True, blank=True)
    city = models.CharField(max_length=127, null=True, blank=True)
    state = models.CharField(max_length=127, null=True, blank=True)
    pin = models.CharField(max_length=6, null=True, blank=True)


    class Meta:
        ordering = ['person__username']

    def __unicode__(self):
        return "{}".format(self.person)


