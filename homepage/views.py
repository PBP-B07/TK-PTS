from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='autentifikasi/login')
def show_main(request):
    context = {
        'page': 'homepage',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
    