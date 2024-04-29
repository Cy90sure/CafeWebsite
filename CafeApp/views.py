from django.shortcuts import render
from .models import Dish
from django.db.models import Q


def index(request):
    Dish_list = Dish.objects.filter(category="dish").order_by("name")

    context = {
        "Dish_list": Dish_list,
        "category" : "ОСНОВНЕ",
    }
    return render(request, "index.html", context)

def desserts_view(request):
    Dish_list = Dish.objects.filter(category="dessert").order_by("name")

    context = {
        "Dish_list": Dish_list,
        "category" : "ДЕСЕРТИ",
    }
    return render(request, "index.html", context)

def cocktails_view(request):
    Dish_list = Dish.objects.filter(category="cocktail").order_by("name")

    context = {
        "Dish_list": Dish_list,
        "category" : "КОКТЕЙЛІ",
    }
    return render(request, "index.html", context)

def search_results(request):
    query = request.GET.get('query', '')
    Dish_list = Dish.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)).order_by("name")

    context = {
        "Dish_list": Dish_list,
        "category" : "ПОШУК ЗА: " + query,
    }
    return render(request, "index.html", context)
