from django.urls import path
from reviews.views import add_reviews_ajax, get_reviews_json, show_review

app_name = 'reviews'

urlpatterns = [
    path('', show_review, name='show_review'),
    path('get-reviews-json/', get_reviews_json, name='get_reviews_json'),
    path('create-reviews-ajax/', add_reviews_ajax, name='add_reviews_ajax')
]