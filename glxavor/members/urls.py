from django.contrib import admin
from django.urls import path, include
from .views import register

urlpatterns = [
    #path('register/', UserRegisterView.as_view(),  name="register"),
    path('register/', register,  name="register"),
]
