from django.urls import path
from book.views import get_books, get_reviews, show_main_book

app_name = 'book'

urlpatterns = [
    path('', get_books, name='get_books'),
    path('book/<int:book_id>/', show_main_book, name='show_main_book'),
    path('review/<int:book_id>/', get_reviews, name='get_reviews'),
]