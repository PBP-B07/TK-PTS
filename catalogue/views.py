from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse
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


...
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))  # Mendapatkan data JSON yang dikirim
        title = data.get("title")
        description = data.get("description")
        author = data.get("author")
        isbn10 = data.get("isbn10")
        isbn13 = data.get("isbn13")
        publish_date = data.get("publish_date")
        edition = data.get("edition")
        best_seller = data.get("best_seller")
        
        # Membuat dan menyimpan objek buku baru
        new_book = Book(
            title=title, description=description, author=author,
            isbn10=isbn10, isbn13=isbn13, publish_date=publish_date,
            edition=edition, best_seller=best_seller
        )
        new_book.save()

        return JsonResponse({"message": "Book added successfully!"}, status=201)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)