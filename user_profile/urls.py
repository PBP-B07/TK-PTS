from django.urls import path
from user_profile.views import show_main, get_profile, get_profile_json, get_ulasan_json

app_name = 'user_profile'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get/', get_profile, name='get_profile'),
    path('get-profile/', get_profile_json, name='get_profile_json'),
    path('get-ulasan/', get_ulasan_json, name='get_ulasan_json'),
]