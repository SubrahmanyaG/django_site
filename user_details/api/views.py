from django.db.models import Q

from user_details.api import serializers
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from user_details.models import UserDetails


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        """
        Return all users
        """
        return User.objects.all()


class UserDetailsViewSet(viewsets.ModelViewSet):
    """
    API for user details
    """
    serializer_class = serializers.UserDetailsSerializer

    def get_queryset(self):
        """
        Return user details for requested user
        Filter based on the username, state, city, pin
        :return:
        """
        username = self.request.query_params.get('username', None)
        state = self.request.query_params.get('state', None)
        city = self.request.query_params.get('city', None)
        pin = self.request.query_params.get('pin', None)
        return UserDetails.objects.filter(Q(person__username=username) | Q(state=state) |
                                          Q(city=city) | Q(pin=pin))