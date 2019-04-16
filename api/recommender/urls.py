from django.urls import include, path

from . import views

urlpatterns = [
    path('recommender/', include([
        path('request/', include([
            path('barc/', views.BarcRequestView.as_view(), name='barc_query'),
        ])),
        path('result/', include([
            path('barc/<str:result_token>/', views.BarcResultView.as_view(), name='barc_result'),
        ])),
    ])),
]
