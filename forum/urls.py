from django.urls import path
from forum.views import show_forum
from forum.views import get_forum_json, add_forum_ajax, get_message_json


app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('get-forum/', get_forum_json, name='get_forum_json'),
    path('get-message/', get_message_json, name='get_message_json'),
    path('create-forum-ajax/', add_forum_ajax, name='add_forum_ajax'),
]