from book.models import Book
from forum.models import Forum, Message
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='')
def show_forum(request):
    forums = Forum.objects.filter(user=request.user)
    context = {
        'forums': forums,
    }
    return render(request, "forum.html", context)

def get_forum_json(request):
    forum_items = Forum.objects.all()
    return HttpResponse(serializers.serialize('json', forum_items))

def get_message_json(request):
    message_items = Message.objects.all()
    return HttpResponse(serializers.serialize('json', message_items))

@csrf_exempt
def add_forum_ajax(request):
    if request.method == 'POST':
        subject = request.POST.get("subject")
        description = request.POST.get("description")
        user = request.user
        book = Book.objects.get(pk=1)

        new_forum = Forum(subject=subject, description=description, user=user, book=book)
        new_forum.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
