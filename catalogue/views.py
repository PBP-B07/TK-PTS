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
        category = request.POST.get("category")
        
        # Membuat dan menyimpan objek buku baru
        new_book = Book(
            title=title, description=description, author=author,
            isbn10=isbn10, isbn13=isbn13, publish_date=publish_date,
            edition=edition, best_seller=best_seller, category=category
        )
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


