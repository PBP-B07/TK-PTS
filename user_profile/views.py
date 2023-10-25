from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from user_profile.models import Profile, UlasanBuatan
from django.core.management import call_command

# Create your views here.
def show_main(request):
    context = {
        'page': 'user profile',
    }

    return render(request, "profile.html", context)

def get_profile(request):
    data = UlasanBuatan.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_ulasan(request):
    data = UlasanBuatan.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def load_my_initial_data(apps, schema_editor):
    call_command("loaddata","fixtures/data.json")

def get_profile_json(request):
    product_item = Profile.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def get_ulasan_json(request):
    product_item = UlasanBuatan.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))