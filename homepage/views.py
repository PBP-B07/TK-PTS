from django.urls import reverse
from homepage.forms import HomepageForm
from reviews.models import Review
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import BookEvent
from book.models import Book
from forum.models import Forum 
from django.db.models import Q

# Create your views here.
# fungsi show main : akan melakukan autentifikasi last login 
@login_required(login_url='autentifikasi/login')
def show_main(request):
    form = HomepageForm()
    
    if 'last_login' not in request.COOKIES:
        return redirect("autentifikasi:login")

    context = {
        'page': 'homepage',
        'last_login': request.COOKIES['last_login'],
        'username': request.user.username,
        'pk' : request.user.pk,
        'book' : Book.objects.all(),
        'form': form
    }
    return render(request, "main.html", context)

# fungsi add event ajax : akan membuat event ajax dengan mengambil berupa title, description, dan book title 
@csrf_exempt
@login_required(login_url='autentifikasi/login')
def add_event_ajax(request):
    form = HomepageForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data.get('title')
        description = form.cleaned_data.get('description')
        book_title = request.POST.get("select-filter")
        book = Book.objects.get(title=book_title)
        new_event = BookEvent(title=title, description=description, book=book)
        new_event.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


# get latest review : mengambil data dari model Review.
# Data diurutkan berdasarkan bidang 'star' secara menurun dan memilih 3 ulasan teratas.
# Data yang diambil kemudian dikonversi menjadi respons JSON menggunakan kelas JsonRespons
# Respons JSON yang dihasilkan akan berisi informasi tentang 3 ulasan teratas, user, star, description dan book title 
@login_required(login_url='autentifikasi/login')
def get_review(request):
    review = Review.objects.order_by('-star')[:3].values(
        'profile__name', 'book__title', 'star', 'description', 'book__pk'
    )
    return JsonResponse(list(review), safe=False)


# fungsi get book : akan mengambil semua objek book 
@login_required(login_url='autentifikasi/login')
def get_book(request):
    book = Book.objects.all()
    return HttpResponse(serializers.serialize("json",book))


# get event : pertama, fungsi ini mengambil semua data dari model BookEvent
# lalu, mengambil values 'book__title', 'title', 'description', 'book', dan 'book__pk'.
# dan dikembalikan dengan respon json 
#@login_required(login_url='autentifikasi/login')
def get_event(request):
    bookEvent = BookEvent.objects.all().values('book__title','title','description','book', 'book__pk')
    return JsonResponse(list(bookEvent), safe=False)


# fungsi get product json : akan memisahkan berdasarkan book kategori
@login_required(login_url='autentifikasi/login')
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

@login_required(login_url='autentifikasi/login')
def get_categories_json(request):
    categories = Book.objects.values_list('category', flat=True).distinct()
    return JsonResponse(list(categories), safe=False)


# get latest forum for one user : fungsi ini akan mengambil semua data dari model Forum
# Data diurutkan berdasarkan tanggal penambahan ('date_added') secara menurun (dari yang paling baru).
# Hanya dua forum teratas yang dipilih menggunakan slicing [:2]
# Lalu, Respons JSON yang dihasilkan akan berisi informasi tentang dua forum terbaru, termasuk nama pengguna,
# subject, user, description 
@login_required(login_url='autentifikasi/login')
def get_forum(request):
    forum = Forum.objects.order_by('-date_added')[:2].values(
        "user","user__username", "date_added", "subject", "description", "pk", "book__title", 'book__pk')
    return JsonResponse(list(forum), safe=False)


# get forum busiest for one user : fungsi ini akan mengambil data dari model Forum
# dan memfilter forum berdasarkan pengguna yang saat ini masuk
# kemudian, hasilnya diurutkan berdasarkan jumlah balasan ('total_reply') secara menurun, 
# dan hanya dua forum teratas yang dipilih menggunakan slicing [:2] 
# dan akan dikembalikan dengan respon json yang berisi informasi tentang dua forum terbusiest
# yang dibuat oleh pengguna yang saat ini masuk, subject, description, 
@login_required(login_url='autentifikasi/login')
def get_busiest_forum(request):
    forum = Forum.objects.filter(user=request.user).order_by('-total_reply')[:2].values(
        "user","user__username", "date_added", "subject", "description", "pk", "book__title", "total_reply", 'book__pk')
    return JsonResponse(list(forum), safe=False)


# get recomended forum for all user : akan mengambil data forum yang direkomendasikan berdasarkan paling banyak peminatnya dari seluruh user
# untuk mengambil data forum yang paling banyak peminat dapat dilihat dari jumlah replies forum tersebut 
# fungsi ini akan mengambil 2 forum yang paling direkomen dengan mengambil values title, username, subject, description
@login_required(login_url='autentifikasi/login')
def get_recomended_forum(request):
    forum = Forum.objects.order_by('-total_reply')[:2].values(
        "user","user__username", "date_added", "subject", "description", "pk", "book__title", "total_reply", 'book__pk')
    return JsonResponse(list(forum), safe=False)


# get not recomended forum for all user : akan mengambil data forum yang tidak direkomendasikan berdasarkan kurang peminatnya dari seluruh user
# untuk mengambil data forum yang kurang peminat dapat dilihat dari jumlah replies forum tersebut 
# fungsi ini akan mengambil 2 forum yang tidak direkomen dengan mengambil values title, username, subject, description
def get_not_recomended_forum(request):
    forum = Forum.objects.order_by('total_reply')[:2].values(
        "user","user__username", "date_added", "subject", "description", "pk", "book__title", "total_reply", 'book__pk')
    return JsonResponse(list(forum), safe=False)