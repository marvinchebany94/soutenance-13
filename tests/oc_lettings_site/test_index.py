import pytest
from django.urls import reverse
from django.test import Client


def test_index_view():
    client = Client()
    #url = "http://127.0.0.1:8000/"
    path = reverse('index')
    response = client.get(path)
    assert response.status_code == 200
