from django.urls import include, path

from . import views

urlpatterns = [
    path('user/', include([
        # path('', views.user_list, name='user_list'),
        path('self/', include([
            path('', views.SelfProfile.as_view(), name='self_profile'),
            path('edit/', views.EditProfile.as_view(), name='edit_profile'),
        ])),
        path('<int:user_pk>/', views.UserDetail.as_view(), name='user_detail'),
    ])),
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('logout/', views.UserLogout.as_view(), name='user_logout'),
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('password/change/', views.UserPasswordChange.as_view(),
         name='user_password_change')
]
