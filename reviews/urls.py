from django.urls import path
from reviews.views import add_reviews_ajax, get_reviews_json, get_user_review, show_review

app_name = 'reviews'

urlpatterns = [
    path('<int:id>', show_review, name='show_review'),
    path('get-reviews-json/<int:id>/', get_reviews_json, name='get_reviews_json'),
    path('create-reviews-ajax/<int:id>/', add_reviews_ajax, name='add_reviews_ajax'), 
    path('get-user-reviews/<int:id>', get_user_review, name='get_user_review'),
]