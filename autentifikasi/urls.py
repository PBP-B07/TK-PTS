from django.urls import path
from autentifikasi.views import register, login_user, logout_user

app_name = 'autentifikasi'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]