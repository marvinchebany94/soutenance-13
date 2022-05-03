from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from lettings import views as lettings_views
from profiles import views as profiles_views

app_name = "oc_lettings_site"
urlpatterns = [
    path('', include('lettings.urls', 'lettings'), name="lettings"),
    path('', include('profiles.urls', 'profiles')),
    #path('lettings/', lettings_views.lettings_index, name='lettings_index'),
    #path('lettings/<int:letting_id>/', lettings_views.letting, name='letting'),
    #path('profiles/', profiles_views.profiles_index, name='profiles_index'),
    #path('profiles/<str:username>/', profiles_views.profile, name='profile'),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
