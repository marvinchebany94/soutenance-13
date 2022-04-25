import pytest

from django.urls import reverse
from django.test import Client
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_index_view():
    client = Client()
    path = reverse('lettings:lettings_index')
    response = client.get(path)
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_view():
    client = Client()
    adresse = Address.objects.create(number=94, street="Saint antoine",
                                     city="Villeneuve saint georges",
                                     state="NY", zip_code=94190,
                                     country_iso_code="USA")
    Letting.objects.create(title="Harry Potter",
                           address=adresse)
    path = reverse('lettings:letting', kwargs={'letting_id': 1})
    response = client.get(path)
    assert response.status_code == 200