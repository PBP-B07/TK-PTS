from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Q  # jangan lupa mengimpor Q
from django.http import JsonResponse  # impor JsonResponse



# Create your views here.
def show_main(request):
    # if 'sort' in request.GET and request.GET['sort'] == 'title':
    #     books = Book.objects.all().order_by('title').values()
    # else:
    #     books = Book.objects.all().order_by('title').values()

    context = {
        'page': 'catalogue',
        # 'books': books,
    }

    return render(request, "show_catalogue.html", context)







def get_product_json(request):
    query = request.GET.get('query', '')  # mendapatkan query pencarian dari parameter GET
    # Jika ada query pencarian, filter buku yang judulnya mengandung query
    if query:
        books = Book.objects.filter(title__icontains=query).order_by('title')
    else:
        # Jika tidak ada query pencarian, ambil semua buku dan urutkan berdasarkan judul
        books = Book.objects.all().order_by('title')
    
    # Mengonversi queryset ke format JSON dan mengembalikannya sebagai respons
    books_json = serializers.serialize('json', books)
    return HttpResponse(books_json)
