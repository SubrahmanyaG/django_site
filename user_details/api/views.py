from django.db.models import Q
from django.http import HttpResponse

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from user_details.api import serializers
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
        ex: http://127.0.0.1:8000/api/userDetails/?pin=560022
        :return:
        """
        username = self.request.query_params.get('username', None)
        state = self.request.query_params.get('state', None)
        city = self.request.query_params.get('city', None)
        pin = self.request.query_params.get('pin', None)
        return UserDetails.objects.filter(Q(person__username=username) | Q(state=state) |
                                          Q(city=city) | Q(pin=pin))
    def create(self, request):
        """
        To create or modify the user Details
        sample post json body
        {
            "username":"Test7",
            "employee_id":132,
            "state": "KERALA",
            "pin":121221

        }
        """
        data = request.data
        user = User.objects.filter(username=data['username']).first()
        if not user:
            user = User(username=data['username'])
            user.save()
        user_detail = UserDetails.objects.filter(person__username=data['username']).first()
        if user_detail:
            user_detail.city = data.get('city')
            user_detail.state = data.get('state')
            user_detail.pin = data.get('pin')
            user_detail.employee_id = data.get('employee_id')
            user_detail.current_address = data.get('current_address')
            user_detail.save()
        else:
            UserDetails.objects.create(person=user,
                                       current_address=data.get('current_address'),
                                       state=data.get('state'),
                                       city=data.get('city'),
                                       pin=data.get('pin'),
                                       employee_id=data.get('employee_id'),
                                       )

        return Response(status=201)
