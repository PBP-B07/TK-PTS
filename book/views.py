import json
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
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

def get_book_json(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book_data = {
        'title': book.title,
        'description': book.description,
        'author': book.author,
        'isbn10': book.isbn10,
        'isbn13': book.isbn13,
        'publish_date': book.publish_date,
        'edition': book.edition,
        'best_seller': book.best_seller,
        'category': book.category,
        'rating': float(book.rating),
    }
    return JsonResponse(book_data)

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

@csrf_exempt
def edit_book_flutter(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        # Get JSON data from the request body
        data = json.loads(request.body)

        # Update book fields with the new data
        book.title = data.get("title", book.title)
        book.description = data.get("description", book.description)
        book.author = data.get("author", book.author)
        book.isbn10 = data.get("isbn10", book.isbn10)
        book.isbn13 = data.get("isbn13", book.isbn13)
        book.publish_date = data.get("publish_date", book.publish_date)
        book.edition = data.get("edition", book.edition)
        book.best_seller = data.get("best_seller", book.best_seller)
        book.category = data.get("category", book.category)

        # Save the updated book
        book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=400)