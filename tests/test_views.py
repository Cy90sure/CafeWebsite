import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CafeWebsite.settings')
import django
django.setup()
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_info_view(client):
    url = reverse('info')
    response = client.get(url)
    assert response.status_code == 200
    assert 'info.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_desserts_view(client):
    url = reverse('desserts')
    response = client.get(url)
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_drinks_view(client):
    url = reverse('drinks')
    response = client.get(url)
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_cocktails_view(client):
    url = reverse('cocktails')
    response = client.get(url)
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_search_results(client):
    url = reverse('search_results')
    response = client.get(url, {'query': 'test'})
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]
