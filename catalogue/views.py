from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'page': 'catalogue',
    }

    return render(request, "show_catalogue.html", context)