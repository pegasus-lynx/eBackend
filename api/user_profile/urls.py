from django.urls import include, path

from . import views

urlpatterns = [
    path('user/', include([
        path('self/', include([
            path('', views.ProfileSelf.as_view(), name='self_detail'),
            path('create/', views.ProfileCreate.as_view(), name='self_create_profile'),
            path('journals/', views.JournalsSelf.as_view(), name='self_journals'),
            path('confrences/', views.ConfrencesSelf.as_view(), name='self_confrences'),
        ])),
        path('<int:user_pk>/', include([
            path('profile/', views.UserDetail.as_view(), name='user_profile'),
            path('journals/', views.UserJournals.as_view(), name='user_journals'),
            path('confrences/', views.UserConfrences.as_view(), name='user_confrences'),
        ])),
    ])),
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('logout/', views.UserLogout.as_view(), name='user_logout'),
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('password/change/', views.UserPasswordChange.as_view(),
         name='user_password_change')
]
