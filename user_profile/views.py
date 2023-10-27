from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from user_profile.models import Profile
from reviews.models import Review
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_main(request):
    context = {
        'page': 'user profile',
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
def delete_review(request, id):
    if request.method == 'POST':
        review = Review.objects.get(pk=id)
        review.delete()
        return HttpResponse("Review deleted successfully", status=200)
    return JsonResponse({"error": "Invalid request method"}, status=400)

def get_reviews(request):
    reviews = Review.objects.filter(user=request.user).values('book__title', 'book__pk', 'pk', 'description', 'star', 'date_added')

    return JsonResponse(list(reviews), safe=False)

def get_review_json(request, id):
    review = Review.objects.filter(pk = id).values('book__title', 'book__pk', 'pk', 'description', 'star', 'date_added')
    return JsonResponse(list(review), safe=False)