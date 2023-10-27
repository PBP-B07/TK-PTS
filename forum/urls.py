from django.urls import path
from forum.views import show_forum
from forum.views import get_forum_json, add_forum_ajax, get_reply_json, add_reply_ajax


app_name = 'forum'

urlpatterns = [
    path('<int:id>/', show_forum, name='show_forum'),
    path('get-forum/<int:id>/', get_forum_json, name='get_forum_json'),
    path('get-reply/<int:id>/', get_reply_json, name='get_reply_json'),
    path('create-forum-ajax/<int:id>/', add_forum_ajax, name='add_forum_ajax'),
    path('create-reply-ajax/<int:id>/', add_reply_ajax, name='add_reply_ajax'),
]