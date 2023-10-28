from book.views import show_main_book
from django.urls import path
from homepage.views import get_event, show_main, create_event, get_book, get_event, add_event_ajax, get_latest_review, get_review


app_name = 'homepage'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_event/', create_event, name='create_event'),
    path('get_book/',get_book,name='get_book'),
    path('book/<int:book_id>/', show_main_book, name='book_detail'),
    path('get_event/', get_event,name='get_event'),
    path('add_event_ajax/',add_event_ajax,name='add_event_ajax'),
    path('get_latest_review/',get_latest_review,name='get_latest_review'),
    path('get_review/',get_review,name='get_review'),
    
]