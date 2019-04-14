from rest_framework import serializers
from django.contrib.auth import authenticate

from .  import models


#  Barc Model Serializers -----------------------------------------------------------------
class BarcSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BarcRequest
        fields = (
            'title', 'abstract', 'created', 'result_token', 'result_generated'
        )
        read_only_fields = (
            'created', 'result_token', 'result_generated'
        )


class BarcResultSerializer(serializers.Serializer):
    query = BarcSerializer()
    top_papers = serializers.ListField(serializers.CharField(max_length=128))
    top_authors = serializers.ListField(serializers.CharField(max_length=32))
    top_confrences = serializers.ListField(serializers.CharField(max_length=128))
    active_areas = serializers.ListField(serializers.CharField(max_length=64))

# ------------------------------------------------------------------------------------------ 

# class LitRecSerializer(serializers.Serializer):
#     pass


# class HDMSerializer(serializers.Serializer):
#     pass


# class EARSerializer(serializers.Serializer):
#     top_keywords = serializers.ListField(child=serializers.CharField(max_length=32),min_length=1,max_length=64)
#     brief_description = serializers.CharField(max_length = 2048)


# class DracorSerializer(serializers.Serializer):
#     pass


# class DiscoverSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length= 256)
#     keywords = serializers.ListField(child=serializers.CharField(max_length=32),min_length=1,max_length=64)
#     abstract = serializers.CharField(max_length = 2048)


# class CnaverSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length= 256)
#     abstract = serializers.CharField(max_length = 2048)


# class ResearchPaperSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             '__all__'
#         )
#         read_only_fields = ( '__all__' )