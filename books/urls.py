from django.urls import path
from books.views import get_books

app_name = 'books'

urlpatterns = [
    path('', get_books, name='get_books'),
]