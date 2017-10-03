from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets
from django.contrib.auth.models import User
from user_details.api import serializers


def get_index_page(request):
    """
    Return to Home
    :return: welcome text
    """
    return HttpResponse('Welcome To Django project')
