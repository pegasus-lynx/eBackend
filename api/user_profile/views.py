from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .models import User

# Create your views here.



class SelfProfile():
    pass

class UserDetail():
    pass

class UserList():
    pass

# class EditProfile():
#     pass