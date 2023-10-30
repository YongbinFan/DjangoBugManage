from django.contrib import admin
from django.urls import path, include
from app01 import views

app_name = 'app01'


urlpatterns = [
    path("register/", views.register, name='register'),
]
