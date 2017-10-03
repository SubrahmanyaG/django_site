from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    serializer class for user object
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
