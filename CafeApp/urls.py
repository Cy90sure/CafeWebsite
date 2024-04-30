from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("info/", views.info_view, name="info"),
    path("", views.index, name="index"),
    path("desserts/", views.desserts_view, name='desserts'),
    path("drinks/", views.drinks_view, name='drinks'),
    path("cocktails/", views.cocktails_view, name='cocktails'),
    path("search/", views.search_results, name='search_results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)