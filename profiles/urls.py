from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
]