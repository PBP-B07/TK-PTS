from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
@login_required(login_url='autentifikasi/login')
def show_main(request):
    if 'last_login' not in request.COOKIES:
        return redirect("autentifikasi:login")

    context = {
        'page': 'homepage',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import BookEvent
from book.models import Book
@login_required(login_url='autentifikasi/login')
def show_events(request):
    events = BookEvent.objects.filter(book_related=True)
    event_list = []
    for event in events:
        event_list.append({
            'title': event.title,
            'description': event.description,
        })
    return JsonResponse({'events': event_list})

@login_required(login_url='autentifikasi/login')
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