from django.shortcuts import render
from reviews.models import Review
from book.models import Book

# Create your views here.
def show_review(request, id):
    books = Book.objects.filter(pk=id) # mengambil objek buku sesuai id
    reviews = Review.objects.filter(book=books[0])
    context = {
               'page' : 'Reviews',
               'reviews' : reviews,
               'title' : books[0]["title"]
    }

    return render(request, "reviews.html", context)