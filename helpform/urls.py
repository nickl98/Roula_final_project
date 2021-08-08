from django.urls import path
from . import views


# url path for team app

urlpatterns = [
    path('', views.team, name='questions'),
]