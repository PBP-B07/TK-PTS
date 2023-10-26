from django.urls import path
from homepage.views import show_main, show_events, create_event, get_book


app_name = 'homepage'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('events/', show_events, name='show_events'),
    path('create_event/', create_event, name='create_event'),
    path('get_book/',get_book,name='get_book'),
]