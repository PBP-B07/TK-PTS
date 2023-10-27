from reviews.models import Review
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import BookEvent
from book.models import Book
from django.db.models import Q

# Create your views here.
@login_required(login_url='autentifikasi/login')
def show_main(request):
    if 'last_login' not in request.COOKIES:
        return redirect("autentifikasi:login")

    context = {
        'page': 'homepage',
        'last_login': request.COOKIES['last_login'],
        'username': request.user.username,
        'pk' : request.user.pk
    }

    return render(request, "main.html", context)


    
@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')

        # Memastikan bahwa pengguna yang membuat event adalah admin
        if not request.user.is_staff:
            return JsonResponse({'status': 'error', 'message': 'Hanya admin yang dapat membuat event.'})

        # Simpan event ke database
        event = BookEvent.objects.create(title=title, description=description, book_related=True)
        event.save()

        return JsonResponse({'status': 'success', 'message': 'Event berhasil disimpan.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Metode permintaan tidak valid.'})

def get_book(request):
    book = Book.objects.filter(id=1)
    return HttpResponse(serializers.serialize("json",book))

def get_event(request):
    bookEvent = BookEvent.objects.all()
    return HttpResponse(serializers.serialize("json",bookEvent))

@csrf_exempt
def add_event_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        book = Book.objects.get(pk=1)

        new_event = BookEvent(title=title, description=description, book=book)
        new_event.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def get_latest_review(request):
    reviews = Review.objects.filter(user=request.user.pk).order_by('-date_added')[:5]
    return HttpResponse(serializers.serialize('json',reviews))

def get_review(request):
    review = Review.objects.all()
    return HttpResponse(serializers.serialize('json',review))

def get_forum(request):
    forum = Review.objects.all()
    return HttpResponse(serializers.serialize('json',review))
