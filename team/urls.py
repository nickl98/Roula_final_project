from django.urls import path
from . import views


# url path for Coach app

urlpatterns = [
    path('', views.team, name='team'),
]