from django.shortcuts import render
from djnago.contrib.auth import login, logout, authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, views

from .permissions import IsOwner
from . import serializers
from .models import User

# Create your views here.

class UserLogin(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserLoginSerializer

    def post(self,request,*args,**kwargs):
        self.request = request
        self.serializer = self.get_serializer()
        self.serializer.is_valid(raise_exception=True)
        
        user = self.serializer.data['user']

        login(request,user)

        return Response({"detail": "User Logged In."}, status=status.HTTP_200_OK)


class UserRegister(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {"detail":'User Registered. Forward to the edit profile page.'},
            status=status.HTTP_201_CREATED)
        


class UserLogout(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            logout(request)
        except Exception as e:
            return Response({'detail': "Could not log out"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail":"Logged out of system."}, status=status.HTTP_200_OK)


class UserPasswordChange(views.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PasswordChangeSerializer

    def post(self, request):
        serialzier = self.get_serializer()
        serialzier.is_valid(raise_exception=True)

        user = request.user

        old_password = serializer.data['old_password']
        new_password = serializer.data['new_password']

        try:
            user.set_password(old_password,new_password)
        except Exception as e:
            return Response({'detail':"Wrong Old Password"},status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': "Password Changed"}, status=status.HTTP_200_OK)


class EditProfile(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = serializers.UserDetailSerializer

    def get_object(self):
        user = self.request.user
        return user

class SelfProfile(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserDetailSerializer

    def get_object(self):
        user = self.request.user
        return user


class UserDetail(generics.RetrieveAPIView):
    permission_classes =  (AllowAny,)
    serializer_class = serializers.UserDetailSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = 'user_pk'


# class UserList(generics.ListAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = 
