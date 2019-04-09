from django.urls import include, path

from . import views

urlpatterns = [
    path('user/', include([
        # path('', views.user_list, name='user_list'),
        path('self/', include([
            path('', views.self_profile, name='self_profile'),
            path('edit/', views.edit_profile, name='edit_profile'),
        ])),
        path('<int:user_pk>/', views.user_detail, name='user_detail'),
    ])),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
    path('password/change/', views.user_password_change,
         name='user_password_change')
]
