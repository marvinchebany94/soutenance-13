from django.urls import reverse
from django.test import Client


def test_index_view():
    client = Client()
    path = reverse('index')
    response = client.get(path)
    assert response.status_code == 200
