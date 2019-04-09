from django.urls import include, path

from . import views

urlpatterns = [
    path('recommender/', include([
        path('barc/', views.BarcView.as_view(), name='barc_view'),
        # Repeat the same lines for other recommender system
        # And make the definitions for views in views.py
    ])
]
