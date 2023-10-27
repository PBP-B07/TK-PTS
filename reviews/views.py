from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from reviews.models import Review
from book.models import Book
from user_profile.models import Profile

# Create your views here.
def show_review(request, id):
    book = Book.objects.get(pk=id) # mengambil objek buku sesuai id
    reviews = Review.objects.filter(book=book)
    context = {
               'page' : 'Reviews',
               'reviews' : reviews,
               'book' : book
    }

    return render(request, "reviews.html", context)

def get_reviews_json(request, id):
    book = Book.objects.get(pk=id)
    reviews = Review.objects.filter(book=book).values('user','profile__name', 'book__title', 'book__pk', 'pk', 'description', 'star', 'date_added')
    
    return JsonResponse(list(reviews), safe=False)
    # return HttpResponse(serializers.serialize('json', reviews))

@csrf_exempt
def add_reviews_ajax(request, id):
    if request.method == 'POST':
        user = request.user
        book = Book.objects.get(pk=id)
        description = request.POST.get("description")
        star = request.POST.get("star")
        profile = Profile.objects.get(user=request.user)

        new_review = Review(user=user, profile=profile, book=book, description=description, star=star)
        new_review.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()