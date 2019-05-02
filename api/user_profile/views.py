from django.shortcuts import render
from django.contrib.auth import login as d_login, logout, authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, views

from .permissions import IsOwner, IsUserAuthenticated
from . import serializers
from . import models

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

# Create your views here.


def create_auth_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token


class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserLoginSerializer

    def get_queryset(self, *args, **kwargs):
        pass

    def login(self):
        validated_data = self.serializer.validated_data
        self.user = validated_data['user']
        d_login(self.request, self.user)
        self.token = create_auth_token(self.user)

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(
            data=request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        self.login()

        return Response(
            {
                "user_id": self.user.pk,
                "token": self.token.key
            },
            status=status.HTTP_200_OK)


class RegisterView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserRegisterSerializer

    def register(self):
        self.user = self.serializer.save()
        self.user.set_password(self.serializer.data['password'])
        self.user.save()
        self.token = create_auth_token(self.user)

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(
            data=request.data, context={'request': request}
        )
        self.serializer.is_valid(raise_exception=True)
        self.register()

        return Response(
            {
                "user_id": self.user.pk,
                "token": self.token.key
            },
            status=status.HTTP_201_CREATED)


class LogoutView(views.APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        print(request.user)
        logout(request)
        print(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetAuthToken(views.APIView):
    pass


class PasswordChangeView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PasswordChangeSerializer

    def post(self, request):
        serialzier = self.get_serializer()
        serialzier.is_valid(raise_exception=True)

        user = None

        old_password = serializer.data['old_password']
        new_password = serializer.data['new_password']

        user = authenticate(username=request.user.username,
                            password=old_password)

        if user == request.user:
            user.set_password(new_password)
        else:
            return Response({'detail': "Wrong Old Password"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': "Password Changed"}, status=status.HTTP_200_OK)


class ProfileCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        validated_data = serializer.validated_data
        profile = models.Profile(user=user, **validated_data)
        profile.save()

        return Response(serializers.ProfileDetailSerializer(profile).data)


class JournalsSelf(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.JournalDetailSerializer

    def get_queryset(self):
        user = self.request.user
        return user.profile.journals_set.all()

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(profile=profile)


class ConfrencesSelf(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ConfrenceDetailSerializer

    def get_queryset(self):
        user = self.request.user
        print(user)
        return user.profile.confrences_set.all()

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(profile=profile)


class UserJournals(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.JournalDetailSerializer
    lookup_url_kwarg = 'user_pk'

    def get_queryset(self):
        user = models.User.objects.get(pk=self.request.kwargs['user_pk'])
        if not user:
            return models.models.QuerySet.none()
        return user.profile.journals_set.all()


class UserConfrences(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ConfrenceDetailSerializer
    lookup_url_kwarg = 'user_pk'

    def get_queryset(self):
        user = models.User.objects.get(pk=self.request.kwargs['user_pk'])
        if not user:
            return models.models.QuerySet.none()
        return user.profile.confrences_set.all()


class ProfileSelf(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProfileDetailSerializer

    def get_object(self):
        user = self.request.user
        return user.profile


class InfoSelf(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserBriefSerializer

    def get_object(self):
        return self.request.user


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserDetailSerializer
    queryset = models.User.objects.all()
    lookup_url_kwarg = 'user_pk'


class UserInfo(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserBriefSerializer
    queryset = models.User.objects.all()
    lookup_url_kwarg = 'user_pk'
