from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from book.models import Book

# Create your views here.
def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data),content_type="application/json")