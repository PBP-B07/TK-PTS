from book.views import show_main_book
from django.urls import path
from homepage.views import get_event, show_main, get_busiest_forum
from homepage.views import get_book, get_event, add_event_ajax, get_review,get_categories_json,get_forum
from homepage.views import get_recomended_forum, get_not_recomended_forum

app_name = 'homepage'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get_book/',get_book,name='get_book'),
    path('book/<int:book_id>/', show_main_book, name='book_detail'),
    path('get_event/', get_event,name='get_event'),
    path('add_event_ajax/',add_event_ajax,name='add_event_ajax'),
    path('get_review/',get_review,name='get_review'),
    path('get_categories/', get_categories_json, name='get_categories'),
    path('get_forum/',get_forum,name='get_forum'),
    path('get_busiest_forum/',get_busiest_forum,name='get_busiest_forum'),
    path('get_recomended_forum/',get_recomended_forum,name='get_recomended_forum'),
    path('get_not_recomended_forum/',get_not_recomended_forum,name='get_not_recomended_forum'),
]