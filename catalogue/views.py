import json
from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.core import serializers
from django.db.models import Q  # jangan lupa mengimpor Q
from django.http import JsonResponse  # impor JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import BookForm

@login_required(login_url='../autentifikasi/login')
# Create your views here.
def show_main(request):
    # if 'sort' in request.GET and request.GET['sort'] == 'title':
    #     books = Book.objects.all().order_by('title').values()
    # else:
    #     books = Book.objects.all().order_by('title').values()
    form = BookForm()
    context = {
        'page': 'catalogue',
        'last_login': request.COOKIES['last_login'],
        'username': request.user.username,
        'pk': request.user.pk,
        'form': form,

        # 'books': books,
    }

    return render(request, "show_catalogue.html", context)

@login_required(login_url='../../autentifikasi/login')
def get_product_json(request):
    query = request.GET.get('query', '')
    category = request.GET.get('category', '')
    sort = request.GET.get('sort', 'title')  # Default sorting by title

    # Starting with all books
    books = Book.objects.all()

    # If there's a search query, filter books that have titles containing the query
    if query:
        books = books.filter(title__icontains=query)

    # If a category is selected, filter books based on category
    if category:
        books = books.filter(category__iexact=category)

    # Sorting books based on the sort parameter
    if sort == 'rating':
        books = books.order_by('-rating', 'title')  # If ratings are equal, sort by title
    elif sort == 'rating_asc':
        books = books.order_by('rating', 'title')   # If ratings are equal, sort by title
    else:
        books = books.order_by('title')

    # Convert the queryset to JSON format and return it as a response
    books_json = serializers.serialize('json', books)
    return HttpResponse(books_json)

@login_required(login_url='../../autentifikasi/login')
def get_categories_json(request):
    categories = Book.objects.values_list('category', flat=True).distinct()
    return JsonResponse(list(categories), safe=False)

@login_required(login_url='../../autentifikasi/login')
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
        rating = request.POST.get("rating")

        # Membuat dan menyimpan objek buku baru
        new_book = Book(
            title=title, description=description, author=author,
            isbn10=isbn10, isbn13=isbn13, publish_date=publish_date,
            edition=edition, best_seller=best_seller, category=category,
            rating=rating
        )
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


# @login_required(login_url='../../autentifikasi/login')
# @csrf_exempt
# def add_product_ajax(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return JsonResponse({"status": "success"}, status=201)
#         else:
#             return JsonResponse({"errors": form.errors}, status=400)
#
#     return HttpResponseNotAllowed(['POST'])

def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Book.objects.create(
            user=request.user,
            title=data["title"],
            description = data["description"],
            author = data["author"],
            isbn10 = data["isbn10"],
            isbn13 = data["isbn13"],
            publish_date = data["publish_date"],
            edition = data["edition"],
            best_seller = data["best_seller"],
            category = data["category"],
            rating = float(data["rating"]),    
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
