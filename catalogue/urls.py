from django.urls import path
from catalogue.views import show_main

app_name = 'catalogue'

urlpatterns = [
    path('', show_main, name='show_main'),
]