from django.urls import path
from .views import item_list, home_page, product_page, checkout_page
app_name = 'core'

urlpatterns = [
    path('', home_page, name='home'),
    path('checkout/', checkout_page, name='checkout'),
    path('product/', product_page, name='product')
]
