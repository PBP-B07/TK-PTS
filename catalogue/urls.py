from django.urls import path
from catalogue.views import create_product_flutter, show_main, get_product_json,add_product_ajax,get_categories_json, is_admin


app_name = 'catalogue'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('get_categories/', get_categories_json, name='get_categories'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('is-admin/', is_admin, name='is_admin'),
]   