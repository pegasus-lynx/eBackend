from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, views

from user_profile.permissions import IsOwner
from user_profile.models import User
from general.utils import get_result, get_result_token

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
        # req.result_token = get_result_token()
        req.save()
        req.result_token = get_result_token(req)
        req.save()

        return Response({'result_token':req.result_token},status=status.HTTP_201_CREATED)


class BarcResultView(generics.RetrieveAPIView):
    permission_classes = (AllowAny, )

    def get_serializer_class(self):
        pass

    def get(self,request, result_token, *args, **kwargs):
        # result_token = self.request.kwargs['result_token']
        print(result_token)
        data = get_result(result_token)
        print(data)
        # return serializers.BarcResultSerializer(**data).data
        return Response({"result":data})
