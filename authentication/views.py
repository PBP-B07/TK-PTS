import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from user_profile.models import Profile


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Successful login status.
            return JsonResponse({
                "username": user.username,
                "status": True,
                # "isAdmin": True,
                "message": "Login successful!"
                # Add other data if you want to send data to Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account disabled."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, check email or password again."
        }, status=401)


@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logged out successfully!"
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout failed."
        }, status=401)


@csrf_exempt
def register(request):
    if request.method == "POST":
        # Extracting values from form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        surname = request.POST.get('surname')
        description = request.POST.get('description')
        is_staff = request.POST.get('admin') == 'true'

        try:
            # Create a new user
            new_user = User.objects.create_user(username=username, password=password, is_staff=is_staff)

            # Create a new profile
            new_profile = Profile.objects.create(user=new_user, name=surname, description=description)

            return JsonResponse({
                "status": True,
                "message": "Account created successfully!",
                "user_id": new_user.id  # Optionally return the created user's ID
            }, status=200)

        except Exception as e:
            return JsonResponse({
                "status": False,
                "message": f"Failed to create user. {str(e)}"
            }, status=500)
    
    return JsonResponse({
        "status": False,
        "message": "Invalid request method."
    }, status=405)