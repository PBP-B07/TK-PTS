from django.urls import path
from reviews.views import show_review

app_name = 'reviews'

urlpatterns = [
    path('<int:id>', show_review, name='show_review'),
]