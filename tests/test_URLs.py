import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CafeWebsite.settings')
import django
django.setup()
import pytest
from django.urls import reverse, resolve
from CafeApp import views


@pytest.mark.django_db
def test_info_url():
    path = reverse('info')
    assert path == '/info/'
    resolver = resolve(path)
    assert resolver.func == views.info_view

@pytest.mark.django_db
def test_index_url():
    path = reverse('index')
    assert path == '/'
    resolver = resolve(path)
    assert resolver.func == views.index

@pytest.mark.django_db
def test_desserts_url():
    path = reverse('desserts')
    assert path == '/desserts/'
    resolver = resolve(path)
    assert resolver.func == views.desserts_view

@pytest.mark.django_db
def test_drinks_url():
    path = reverse('drinks')
    assert path == '/drinks/'
    resolver = resolve(path)
    assert resolver.func == views.drinks_view

@pytest.mark.django_db
def test_cocktails_url():
    path = reverse('cocktails')
    assert path == '/cocktails/'
    resolver = resolve(path)
    assert resolver.func == views.cocktails_view

@pytest.mark.django_db
def test_search_results_url():
    path = reverse('search_results')
    assert path == '/search/'
    resolver = resolve(path)
    assert resolver.func == views.search_results
