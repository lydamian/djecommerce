from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order
# Create your views here.


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


class HomeView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.create(item=item)
