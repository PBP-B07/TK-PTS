from django.urls import path
from book.views import get_books,edit_book, show_main_book
app_name = 'book'

urlpatterns = [
    path('', get_books, name='get_books'),
    path('<int:book_id>/', show_main_book, name='show_main_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
]