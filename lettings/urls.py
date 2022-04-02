from django.contrib import admin
from django.urls import path
from . import views

app_name = 'oc_lettings_site'
urlpatterns = [
    path('lettings/', views.lettings_index),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
]