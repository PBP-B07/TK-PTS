from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from autentifikasi.forms import ProfileForm

# Import the CustomUserCreationForm at the top of your views.py file
from .forms import CustomUserCreationForm

# Your existing code remains unchanged, just replace UserCreationForm with CustomUserCreationForm
@csrf_exempt
def register(request):
    form = CustomUserCreationForm()
    form_profile = ProfileForm(request.POST or None)

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid() and form_profile.is_valid():
            user = form.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('autentifikasi:login')
    context = {'form': form, 'form_profile': form_profile}
    return render(request, 'register.html', context)


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("homepage:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('autentifikasi:login'))
    response.delete_cookie('last_login')
    return response
