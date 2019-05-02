# from drf_yasg.utils import swagger_serializer_method
import re
from rest_framework import serializers
from django.contrib.auth import login, logout, authenticate
from drf_yasg.utils import swagger_serializer_method


from . import models


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32, required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        user = None

        if username and password:
            user = authenticate(username=username, password=password)
        else:
            raise serializers.ValidationError('Incomplete Credentials')

        if not user:
            raise serializers.ValidationError('Wrong Credentials')

        data['user'] = user
        return data


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32, required=True)
    first_name = serializers.CharField(max_length=32, required=True)
    last_name = serializers.CharField(max_length=32, required=False)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=32, required=True)

    def create(self, validated_data):
        return models.User(**validated_data)


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=32, required=True)
    new_password = serializers.CharField(max_length=32, required=True)
    confirm_password = serializers.CharField(max_length=32, required=True)


class JournalBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Journals
        fields = (
            'title', 'year', 'journal'
        )


class ConfrenceBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Confrences
        fields = (
            'title', 'year'
        )


class ProfileDetailSerializer(serializers.ModelSerializer):
    journals = serializers.SerializerMethodField()
    confrences = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
        fields = (
            'role', 'bio', 'gender',
            'department', 'institution',
            'dob', 'area_of_interest',
            'journals', 'confrences'
        )

    @swagger_serializer_method(JournalBriefSerializer(many=True))
    def get_journals(self, obj):
        return JournalBriefSerializer(obj.journals_set.all(), many=True).data

    @swagger_serializer_method(ConfrenceBriefSerializer(many=True))
    def get_confrences(self, obj):
        return ConfrenceBriefSerializer(obj.confrences_set.all(), many=True).data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = (
            'role', 'bio', 'gender',
            'department', 'institution',
            'dob', 'area_of_interest'
        )


class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileDetailSerializer()

    class Meta:
        model = models.User
        fields = (
            'pk', 'username', 'email', 'full_name', 'profile'
        )
        read_only_fields = (
            'username', 'email', 'full_name', 'profile'
        )


class UserBriefSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    institution = serializers.SerializerMethodField()
    dob = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        fields = (
            'pk', 'full_name', 'email', 'dob', 'role', 'institution'
        )

    @swagger_serializer_method(serializers.CharField(max_length=20))
    def get_dob(self, obj):
        return obj.profile.dob

    @swagger_serializer_method(serializers.ChoiceField(choices=[0, 1, 2, 3]))
    def get_role(self, obj):
        return obj.profile.role

    @swagger_serializer_method(serializers.CharField(max_length=20))
    def get_institution(self, obj):
        return obj.profile.institution


class JournalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Journals
        fields = (
            'title', 'year', 'authors_list', 'journal', 'indexed_in'
        )


class ConfrenceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Confrences
        fields = (
            'title', 'year', 'authors_list', 'description'
        )


class ProfileLinksDetailSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.ProfileLinks
        fields = (
            'link_linked_in', 'link_research_gate', 'link_google_scholar', 'link_dblp', 'link_github', 'link_publons',
        )
