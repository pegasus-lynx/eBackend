from django.shortcuts import render
from django.shortcuts import render
from djnago.contrib.auth import login, logout, authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, views

from user_profile.permissions import IsOwner
from user_profile.models import User

from . import serializers
# Create your views here.

class BarcRequestView(generics.GenericAPIView):
    pass


class BarcResultView(generics.RetrieveAPIView):
    pass