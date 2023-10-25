from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from books.models import Books

def get_books(request):
    data = Books.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")