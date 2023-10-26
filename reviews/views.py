from django.shortcuts import render
from reviews.models import Review
from books.models import Books

# Create your views here.
def show_review(request, id):
    books = Books.objects.filter(pk=id) # mengambil objek buku sesuai id
    reviews = Review.objects.filter(book=books)
    context = {
               'page' : 'Reviews',
               'reviews' : reviews,
               'title' : books["title"]
    }

    return render(request, "reviews.html", context)