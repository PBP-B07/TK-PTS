from book.views import show_main_book
from django.urls import path
from homepage.views import get_event, show_main, create_event, get_book, get_event, add_event_ajax, get_review,get_categories_json


app_name = 'homepage'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_event/', create_event, name='create_event'),
    path('get_book/',get_book,name='get_book'),
    path('book/<int:book_id>/', show_main_book, name='book_detail'),
    path('get_event/', get_event,name='get_event'),
    path('add-event-ajax/',add_event_ajax,name='add_event_ajax'),
    path('get-review/',get_review,name='get_review'),
    path('get_categories/', get_categories_json, name='get_categories'),
    
]