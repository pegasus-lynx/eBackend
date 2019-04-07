from django.urls import include, path

from . import views

urlpatterns = [
    path('user/', include([
        path('', views.UserList.as_view(), name='user_list'),
        path('self/', include([
            path('',views.SelfProfile.as_view(), name='self_profile'),
            path('edit/',views.EditProfile.as_view(), name='edit_profile'),
        ])),
        path('<int:user_pk>/',views.UserDetail.as_view(),name='user_detail'),
    ]))
]