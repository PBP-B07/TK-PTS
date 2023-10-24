from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'page': 'user profile',
    }

    return render(request, "profile.html", context)