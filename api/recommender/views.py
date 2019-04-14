from django.shortcuts import render
from django.shortcuts import render
from djnago.contrib.auth import login, logout, authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, views

from user_profile.permissions import IsOwner
from user_profile.models import User
from general.utils import get_result

from . import serializers
from . import models
# Create your views here.

class BarcRequestView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = serializers.BarcSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        req = models.BarcRequest(**validated_data)
        req.result_token = req.get_result_token()
        req.save()

        return Response({'result_token':req.result_token},status=status.HTTP_201_CREATED)


class BarcResultView(generics.RetrieveAPIView):
    permission_classes = (AllowAny, )

    def get(self):
        result_token = self.request.kwargs['result_token']
        data = get_result(result_token)
        return data
