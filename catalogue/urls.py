from django.urls import path
from catalogue.views import show_main, get_product_json


app_name = 'catalogue'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-product/', get_product_json, name='get_product_json'),
]