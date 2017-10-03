from django.contrib.auth.models import User

from rest_framework import serializers

from user_details.models import UserDetails


class UserSerializer(serializers.ModelSerializer):
    """
    serializer class for user object
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    serializer class for userDetails object
    """
    person = UserSerializer()

    class Meta:
        model = UserDetails
        fields = ('person', 'date_of_birth', 'employee_id', 'current_address', 'city', 'state', 'pin')


class test(serializers.ModelSerializer):
    """
    serializer class for userDetails object
    """
    class Meta:
        model = UserDetails
        fields = ('date_of_birth', 'employee_id', 'current_address', 'city', 'state', 'pin')