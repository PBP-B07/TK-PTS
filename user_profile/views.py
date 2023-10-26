from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import render
from user_profile.models import Profile
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