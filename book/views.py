from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from book.models import Book

@login_required(login_url='../../autentifikasi/login')
def show_main_book(request, book_id):
    
    book = get_object_or_404(Book, pk=book_id)

    context = {
        'page': 'Book Description',
        'book': book, 
    }

    return render(request, "book.html", context)

def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data),content_type="application/json")

@csrf_exempt
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        # Ambil data yang diedit dari permintaan POST
        book.title = request.POST.get("title")
        book.description = request.POST.get("description")
        book.author = request.POST.get("author")
        book.isbn10 = request.POST.get("isbn10")
        book.isbn13 = request.POST.get("isbn13")
        book.publish_date = request.POST.get("publish_date")
        book.edition = request.POST.get("edition")
        book.best_seller = request.POST.get("best_seller")
        book.category = request.POST.get("category")
        
        # Edit data buku
        book.save()
        return HttpResponse(status=201)  # Berhasil mengedit buku
    return HttpResponse(status=400)  # Gagal mengedit buku
