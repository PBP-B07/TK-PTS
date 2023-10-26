from django.urls import path
from user_profile.views import show_main, get_profile_json, get_profile, edit_profile_ajax

app_name = 'user_profile'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-profile/', get_profile_json, name='get_profile_json'),
    path('get/', get_profile, name = 'get_profile'),
    path('edit/', edit_profile_ajax, name='edit_profile_ajax')
]