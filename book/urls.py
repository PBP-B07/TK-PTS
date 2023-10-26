from django.urls import path
from book.views import get_books, show_main_book

app_name = 'book'

urlpatterns = [
    path('', get_books, name='get_books'),
    path('book/<int:book_id>/', show_main_book, name='show_main_book'),
]