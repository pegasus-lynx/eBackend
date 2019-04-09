from rest_framework import serializers
from django.contrib.auth import authenticate

class BarcSerializer(serializers.Serializer):
    pass


class LitRecSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=2048)
    Abstract=serializers.CharField(max_length = 2048)


class HDMSerializer(serializers.Serializer):
    pass


class EARSerializer(serializers.Serializer):
    top_keywords = serializers.ListField(child=serializers.CharField(max_length=32),min_length=1,max_length=64)
    brief_description = serializers.CharField(max_length = 2048)


class DracorSerializer(serializers.Serializer):
    Target=serializers.CharField(max_length = 2048)
    Authors=serializers.ListField(child=serializers.CharField(max_length=32),min_length=1,max_length=64)


class DiscoverSerializer(serializers.Serializer):
    title = serializers.CharField(max_length= 256)
    keywords = serializers.ListField(child=serializers.CharField(max_length=32),min_length=1,max_length=64)
    abstract = serializers.CharField(max_length = 2048)


class CnaverSerializer(serializers.Serializer):
    title = serializers.CharField(max_length= 256)
    abstract = serializers.CharField(max_length = 2048)