from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from book.models import Book

def show_main_book(request, book_id):
    
    book = get_object_or_404(Book, pk=book_id)

    context = {
        'page': 'Deskripsi',
        'book': book, 
    }

    return render(request, "book.html", context)

def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data),content_type="application/json")