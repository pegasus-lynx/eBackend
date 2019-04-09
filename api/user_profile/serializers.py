# from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from django.contrib.auth import authenticate


from .models import User

class TokenSerializer(serializers.Serializer):
    token = serializers.ReadOnlyField()

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32,required=False)
    password = serializers.CharField(required=False)

    def validate(self,attrs):
        username = attrs.get('username', None)
        password = attrs.get('password', None)

        user = None

        if username and password:
            user = authenticate(username=username, password=password)
        else:
            raise serializers.ValidationError('Incomplete Credentials')

        if not user:
            raise serializers.ValidationError('Wrong Credentials')

        attrs['user'] = user
        return attrs


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32,required=True)
    first_name = serializers.CharField(max_length=32, required=True)
    lest_name = serializers.CharField(max_length = 32, required = False)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=32,required=True)

    def validate_username(self, attrs):
        pass

    def validate_password(self,attrs):
        pass

    def validate_email(self, attrs):
        pass

    def validate(self,attrs):
        pass

    def save(self, attrs):
        pass


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=32, required=True)
    new_password = serializers.CharField(max_length=32, required=True)
    confirm_password  =serializers.CharField(max_length=32, required=True)

    def validate_password(self, attrs):
        pass

    

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


class JournalDetailSerializer(serialziers.ModelSerializer):
    pass


class ConfrenceDetailSerializer(serializers.ModelSerializer):
    pass
