from django.urls import path
from user_profile.views import show_main

app_name = 'user_profile'

urlpatterns = [
    path('', show_main, name='show_main'),
]