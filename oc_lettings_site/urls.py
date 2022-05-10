from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "oc_lettings_site"
urlpatterns = [
    path('', include('lettings.urls', 'lettings'), name="lettings"),
    path('', include('profiles.urls', 'profiles')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
