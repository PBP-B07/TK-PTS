from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.core import serializers
from django.db.models import Q  # jangan lupa mengimpor Q
from django.http import JsonResponse  # impor JsonResponse
from django.views.decorators.csrf import csrf_exempt



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




@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        author = request.POST.get("author")
        isbn10 = request.POST.get("isbn10")
        isbn13 = request.POST.get("isbn13")
        publish_date = request.POST.get("publish_date")
        edition = request.POST.get("edition")
        best_seller = request.POST.get("best_seller")
        
        # Membuat dan menyimpan objek buku baru
        new_book = Book(
            title=title, description=description, author=author,
            isbn10=isbn10, isbn13=isbn13, publish_date=publish_date,
            edition=edition, best_seller=best_seller
        )
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()