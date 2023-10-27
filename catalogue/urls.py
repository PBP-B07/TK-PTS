from django.urls import path
from catalogue.views import show_main, get_product_json,add_product_ajax


app_name = 'catalogue'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax')
]