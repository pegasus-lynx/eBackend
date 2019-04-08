from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .models import User

# Create your views here.


class SelfProfile(generics.ListCreateAPIView):
    pass


class UserDetail(generics.ListCreateAPIView):
    pass


class UserList(generics.ListCreateAPIView):
    pass


class UserLogin(generics.ListCreateAPIView):
    pass


class UserRegister(generics.ListCreateAPIView):
    pass


class UserLogout(generics.ListCreateAPIView):
    pass


class UserPasswordChange(generics.ListCreateAPIView):
    pass


class EditProfile(generics.ListCreateAPIView):
    pass
