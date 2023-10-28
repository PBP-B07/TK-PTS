from django.urls import path
from user_profile.views import show_main, get_profile_json, get_profile, edit_profile_ajax, get_reviews, delete_review, get_review_json, edit_review_ajax

app_name = 'user_profile'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-profile/', get_profile_json, name='get_profile_json'),
    path('get/', get_profile, name = 'get_profile'),
    path('edit/', edit_profile_ajax, name='edit_profile_ajax'),
    path('reviews/', get_reviews, name='get_reviews'),
    path('delete_review/<int:id>/', delete_review, name='delete_review'),
    path('get_review/<int:id>/', get_review_json, name='get_review_json'),
    path('edit_review/<int:id>/', edit_review_ajax, name='edit_review_ajax'),
]