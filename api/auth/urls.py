from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('logout/', views.UserLogout.as_view(), name='user_logout'),
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('password/change/',views.UserPasswordChange.as_view(), name='user_password_change')
]
