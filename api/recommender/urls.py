from django.urls import include, path

from . import views

urlpatterns = [
    path('recommender/', include([
        path('barc/', views.BarcView.as_view(), name='barc_view'),
        path('litrec/', views.LitRecView.as_view(), name='litrec_view'),
        path('ear/', views.EARView.as_view(), name='ear_view'),
        path('hdm/', views.HDMView.as_view(), name='hdm_view'),
        path('dracor/', views.DracorView.as_view(), name='dracor_view'),
        path('discover/', views.DiscoverView.as_view(),  name='discover_view'),
        path('cnaver/', views.Cnaver.as_view(), name='cnaver_view'),
    ])
]
