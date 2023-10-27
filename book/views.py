from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from book.models import Book
from reviews.models import Review

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

@csrf_exempt
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        # Ambil data yang diedit dari permintaan POST
        name = request.POST.get("name")
        description = request.POST.get("description")

        # Edit data buku
        book.name = name
        book.description = description
        book.save()

        return HttpResponse(status=201)  # Berhasil mengedit buku

    return HttpResponse(status=400)  # Gagal mengedit buku

# def get_reviews(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     reviews = Review.objects.filter(book=book)
#     return HttpResponse(serializers.serialize("json", reviews),content_type="application/json")

def get_reviews(request, book_id):
    reviews = Review.objects.filter(book_id=book_id)[:5]  # Mengambil 5 review pertama
    review_data = [{'text': review.description, 'author': review.user} for review in reviews]
    return JsonResponse(review_data, safe=False)

def show_reviews(request, book_id):
    reviews = Review.objects.filter(book_id=book_id)
    context = {
        'reviews': reviews,
    }
    return render(request, "reviews.html", context)
