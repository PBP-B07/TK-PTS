from django.shortcuts import render
from book.models import Book



# Create your views here.
def show_main(request):
    if 'sort' in request.GET and request.GET['sort'] == 'title':
        books = Book.objects.all().order_by('title').values()
    else:
        books = Book.objects.all().values()

    context = {
        'page': 'catalogue',
        'books': books,
    }

    return render(request, "show_catalogue.html", context)




