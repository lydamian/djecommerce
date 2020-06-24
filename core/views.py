from django.shortcuts import render
from .models import Item
# Create your views here.


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "item-list.html", context)


def home_page(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home-page.html", context)


def checkout_page(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "checkout-page.html", context)


def product_page(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product-page.html", context)
