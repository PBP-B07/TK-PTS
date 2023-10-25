from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'page': 'homepage',
    }

    return render(request, "main.html", context)
    