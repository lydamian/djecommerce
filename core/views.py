from django.shortcuts import render
from .models import Item
# Create your views here.


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "item-list.html", context)


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home.html", context)


def checkout(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "checkout.html", context)


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)
