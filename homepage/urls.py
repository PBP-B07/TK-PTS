from django.urls import path
from homepage.views import show_main

app_name = 'homepage'

urlpatterns = [
    path('', show_main, name='show_main'),
]