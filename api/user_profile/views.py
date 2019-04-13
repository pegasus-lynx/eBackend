from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, views
from rest_framework.authtoken.models import Token

from .permissions import IsOwner, IsUserAuthenticated
from . import serializers
from . import models

# Create your views here.

class UserLogin(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserLoginSerializer

    def post(self,request,*args,**kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=request.data, context={'request':request})
        self.serializer.is_valid(raise_exception=True)
        
        print('-'*200)

        validated_data = self.serializer.validated_data
        user = validated_data['user']

        login(request,user)

        return Response({"detail": "User Logged In."}, status=status.HTTP_200_OK)


class UserRegister(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(serializer.data['password'])
        user.save()

        return Response(
            {"detail":'User Registered. Forward to the edit profile page.\n'},
            status=status.HTTP_201_CREATED)
        


class UserLogout(views.APIView):
    permission_classes = (IsUserAuthenticated,)

    def post(self, request):
        try:
            logout(request)
        except Exception as e:
            return Response({'detail': "Could not log out"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail":"Logged out of system."}, status=status.HTTP_200_OK)


class UserPasswordChange(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PasswordChangeSerializer

    def post(self, request):
        serialzier = self.get_serializer()
        serialzier.is_valid(raise_exception=True)

        user = None

        old_password = serializer.data['old_password']
        new_password = serializer.data['new_password']

        user = authenticate(username=request.user.username, password=old_password)

        if user == request.user:
            user.set_password(new_password)
        else:
            return Response({'detail':"Wrong Old Password"},status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': "Password Changed"}, status=status.HTTP_200_OK)


class ProfileCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProfileDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile = models.Profile(**validated_data)
        profile.save()

        return profile


class ProfileSelf(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProfileDetailSerializer

    def get_object(self):
        user = self.request.user
        return user.profile

class UserDetail(generics.RetrieveAPIView):
    permission_classes =  (AllowAny,)
    serializer_class = serializers.UserDetailSerializer
    queryset = models.User.objects.all()
    lookup_url_kwarg = 'user_pk'

