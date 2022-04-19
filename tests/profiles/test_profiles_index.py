import pytest

from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index():
    client = Client()
    path = reverse('profiles:profiles_index')
    response = client.get(path)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_index_with_username():
    client = Client()
    User.objects.create(username="marvin94", last_name="chebany",
                        email="marvin@gmail.com", first_name="marvin", id=1)
    Profile.objects.create(favorite_city="Buenos Aires",
                           user_id=1)
    path = reverse('profiles:profile', kwargs={'username': 'marvin94'})
    response = client.get(path)
    assert response.status_code == 200