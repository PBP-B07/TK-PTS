from reviews.models import Review
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import BookEvent
from book.models import Book
from forum.models import Forum 
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
        'pk' : request.user.pk,
        'book' : Book.objects.all()
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

@csrf_exempt
def add_event_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        book_title = request.POST.get("select-filter")
        book = Book.objects.get(title=book_title)
        new_event = BookEvent(title=title, description=description, book=book)
        new_event.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def get_review(request):
    review = Review.objects.order_by('-star')[:3].values(
        'profile__name', 'book__title', 'star', 'description'
    )
    return JsonResponse(list(review), safe=False)

def get_book(request):
    book = Book.objects.all()
    return HttpResponse(serializers.serialize("json",book))

def get_event(request):
    bookEvent = BookEvent.objects.all().values('book__title','title','description','book')
    return JsonResponse(list(bookEvent), safe=False)

def get_product_json(request):
    query = request.GET.get('query', '')  # mendapatkan query pencarian dari parameter GET
    category = request.GET.get('category', '')  # mendapatkan kategori dari parameter GET
    
    # Memulai dengan semua buku
    books = Book.objects.all()
    
    # Jika ada query pencarian, filter buku yang judulnya mengandung query
    if query:
        books = books.filter(title__icontains=query)
    
    # Jika ada kategori yang dipilih, filter buku berdasarkan kategori
    if category:
        books = books.filter(category__iexact=category)  # Assuming your field name is 'category'
    
    # Mengurutkan buku berdasarkan judul
    books = books.order_by('title')
    
    # Mengonversi queryset ke format JSON dan mengembalikannya sebagai respons
    books_json = serializers.serialize('json', books)
    return HttpResponse(books_json)

def get_categories_json(request):
    categories = Book.objects.values_list('category', flat=True).distinct()
    return JsonResponse(list(categories), safe=False)

def get_forum(request):
    forum = Forum.objects.order_by('-star')[:3].values(
        'profile__name', 'book__title', 'star', 'description'
    )
    return JsonResponse(list(forum), safe=False)
