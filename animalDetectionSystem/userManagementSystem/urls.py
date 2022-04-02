# from django.contrib import admin
from . import views
from django.urls import path
from .views import UserRegisterView, home

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('home/',views.home,name="home"),
]

