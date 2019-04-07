from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from .models import User

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk', 'username', 'email', 'full_name', 'gender', 'bio',
            'institution', 'department', 'dob', 'role' 
        )
        read_only_fields = (
            'username', 'email', 'gender', 'full_name' 
        )

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk', 'full_name', 'bio', 'role', 'institution'
        )

class UserBreifSerializer():
    pass
