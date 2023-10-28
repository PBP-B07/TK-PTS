from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from user_profile.models import Profile
from reviews.models import Review
from book.models import Book
from forum.models import Forum, Reply
from django.views.decorators.csrf import csrf_exempt
from user_profile.forms import ReviewForm

# Create your views here.
def show_main(request):
    form_review = ReviewForm(request.POST or None)
    context = {
        'page': 'user profile',
        'form_review': form_review,
        'user': request.user,

    }

    return render(request, "profile.html", context)

def get_profile_json(request):
    profile = Profile.objects.all()
    return HttpResponse(serializers.serialize('json', profile))

def get_profile(request):
    profile = Profile.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', profile))

@csrf_exempt
def edit_profile_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")

        profile = Profile.objects.get(user=request.user)
        profile.name = name
        profile.description = description
        profile.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def edit_review_ajax(request,id):
    form_review = ReviewForm(request.POST or None)
    if request.method == 'POST' and form_review.is_valid():
        description = form_review.cleaned_data.get('description')
        star = request.POST.get("star")

        review = Review.objects.get(pk=id)
        review.description = description

        rating_lama = review.star

        review.star = star
        review.save()

        perubahan = int(review.star) - int(rating_lama)
        book = Book.objects.get(pk=review.book.pk)
        review_book = Review.objects.filter(book=book)
        newrating = newrating = (book.rating*len(review_book) + perubahan)/len(review_book)
        book.rating=newrating
        book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_review(request, id):
    if request.method == 'POST':
        review = Review.objects.get(pk=id)

        book = Book.objects.get(pk=review.book.pk)
        review_book = Review.objects.filter(book=book)
        if len(review_book) == 1:
            newrating = 0
        else:
            newrating = (book.rating*len(review_book) - review.star)/len(review_book)-1
        
        book.rating=newrating
        book.save()

        review.delete()
        return HttpResponse("Review deleted successfully", status=200)
    return JsonResponse({"error": "Invalid request method"}, status=400)

def get_reviews(request):
    reviews = Review.objects.filter(user=request.user).values('book__rating','book__title', 'book__pk', 'pk', 'description', 'star', 'date_added').order_by('-pk')

    return JsonResponse(list(reviews), safe=False)

def get_review_json(request, id):
    review = Review.objects.filter(pk = id).values('book__rating','book__title', 'book__pk', 'pk', 'description', 'star', 'date_added')
    return JsonResponse(list(review), safe=False)

def get_forum(request):
    forum = Forum.objects.filter(user=request.user).values('book__title', 'pk', 'subject', 'description', 'date_added')
    return JsonResponse(list(forum), safe=False)

def get_reply(request):
    reply = Reply.objects.filter(user=request.user).values('forum__subject', 'message', 'forum__user__username', 'forum__user__pk', 'pk')
    return JsonResponse(list(reply), safe=False)

def get_reply_json(request, id):
    reply = Reply.objects.filter(pk = id).values('forum__subject', 'message', 'forum__user__username', 'forum__user__pk', 'pk')
    return JsonResponse(list(reply), safe=False)