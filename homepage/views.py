from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'page': 'homepage',
    }

    return render(request, "main.html", context)