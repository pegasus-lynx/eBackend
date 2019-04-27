from django.urls import include, path

from . import views

urlpatterns = [
    path('user/', include([
        path('self/', include([
            path('', views.ProfileSelf.as_view(), name='self_detail'),
            path('info/', views.InfoSelf.as_view(), name="self_breif_info"),
            path('create/', views.ProfileCreate.as_view(),
                 name='self_create_profile'),
            path('journals/', views.JournalsSelf.as_view(), name='self_journals'),
            path('confrences/', views.ConfrencesSelf.as_view(),
                 name='self_confrences'),
        ])),
        path('<int:user_pk>/', include([
            path('info/', views.UserInfo.as_view(), name='user_breif'),
            path('profile/', views.UserDetail.as_view(), name='user_profile'),
            path('journals/', views.UserJournals.as_view(), name='user_journals'),
            path('confrences/', views.UserConfrences.as_view(),
                 name='user_confrences'),
        ])),
    ])),
    path('login/', views.LoginView.as_view(), name='user_login'),
    path('logout/', views.LogoutView.as_view(), name='user_logout'),
    path('register/', views.RegisterView.as_view(), name='user_register'),
    path('password/change/', views.PasswordChangeView.as_view(),
         name='user_password_change'),
    path('auth/token/', views.GetAuthToken.as_view(), name='get_auth_token'),
]
