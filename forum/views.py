from book.models import Book
from forum.models import Forum, Reply
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='')
def show_forum(request, id):
    book = Book.objects.get(pk=id)
    forums = Forum.objects.filter(user=request.user)
    context = {
        'forums': forums,
        'book':  book,
    }
    return render(request, "forum.html", context)

def get_forum_json(request,id):
    book = Book.objects.get(pk=id)
    forum_items = Forum.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', forum_items))

def get_reply_json(request,id):
    forum = Forum.objects.filter(pk=id)
    message_items = Reply.objects.filter(forum=forum)
    return HttpResponse(serializers.serialize('json', message_items))

@csrf_exempt
def add_forum_ajax(request,id):
    if request.method == 'POST':
        subject = request.POST.get("subject")
        description = request.POST.get("description")
        user = request.user
        book = Book.objects.get(pk=id)

        new_forum = Forum(subject=subject, description=description, user=user, book=book)
        new_forum.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def add_reply_ajax(request,id):
    if request.method == 'POST':
        message = request.POST.get("message")
        user = request.user
        book = Book.objects.get(pk=id)
        forum = Forum.objects.filter(pk=id)

        new_reply = Reply(message=message, user=user, book=book, forum=forum)
        new_reply.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()