from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from reviews.forms import ReviewForm
from reviews.models import Review
from book.models import Book
from user_profile.models import Profile

# Create your views here.
@login_required(login_url=('../autentifikasi/login'))
def show_review(request, id):
    book = Book.objects.get(pk=id) # mengambil objek buku sesuai id
    reviews = Review.objects.filter(book=book)
    form = ReviewForm()
    context = {
               'page' : 'Reviews',
               'reviews' : reviews,
               'book' : book,
               'form' : form,
    }

    return render(request, "reviews.html", context)

def get_reviews_json(request, id):
    filters = request.GET.get('filter', '')
    book = Book.objects.get(pk=id)
    reviews = Review.objects.filter(book=book).values('user','profile__name', 'book__title', 'book__pk', 'pk', 'description', 'star', 'date_added')

    if (filters):
        if (filters == "date"):
            reviews = reviews.order_by('date_added')
        else :
            reviews = Review.objects.filter(book=book, star=filters).values('user','profile__name', 'book__title', 'book__pk', 'pk', 'description', 'star', 'date_added')
            reviews = reviews.order_by('date_added')

    return JsonResponse(list(reviews), safe=False)

def get_user_review(request, id):
    book = Book.objects.get(pk=id)
    reviews = Review.objects.filter(book=book, user=request.user).values('user','profile__name', 'book__title', 'book__pk', 'pk', 'description', 'star', 'date_added')

    return JsonResponse(list(reviews), safe=False)

@csrf_exempt
def add_reviews_ajax(request, id):
    if request.method == 'POST':
        user = request.user
        book = Book.objects.get(pk=id)
        reviews = Review.objects.filter(book=book)

        star = int(request.POST.get("star"))
        rate = (book.rating*len(reviews)+star)/(len(reviews)+1)
        book.rating = rate
        book.save()

        description = request.POST.get("description")
        profile = Profile.objects.get(user=request.user)

        new_review = Review(user=user, profile=profile, book=book, description=description, star=star)
        new_review.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()