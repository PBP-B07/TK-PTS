import json
from book.models import Book
from forum.forms import ForumForm
from forum.models import Forum, Reply
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime
from forum.models import Forum

@login_required(login_url=('../../autentifikasi/login'))
def show_forum(request, id):
    book = Book.objects.get(pk=id)
    forums = Forum.objects.filter(user=request.user)
    form = ForumForm()
    context = {
        'forums': forums,
        'book':  book,
        'last_login': request.COOKIES['last_login'],
        'username': request.user.username,
        'pk': request.user.pk,
        'form': form,
    }
    return render(request, "forum.html", context)

def get_forum_json(request,id):
    book = Book.objects.get(pk=id)
    forum_items = Forum.objects.filter(book=book).values("user","user__username", "date_added", "subject", "description", "pk")
    return JsonResponse(list(forum_items), safe=False)

def get_reply_json(request,bookid,id):
    book = Book.objects.get(pk=bookid)
    forum = Forum.objects.get(pk=id)
    message_items = Reply.objects.filter(forum=forum).values("user","user__username", "message", "pk")
    message_items = message_items.order_by('pk')
    return JsonResponse(list(message_items), safe=False)

@csrf_exempt
def add_forum_ajax(request,id):
    if request.method == 'POST':
        subject = request.POST.get("subject").strip()
        description = request.POST.get("description").strip()
        user = request.user
        book = Book.objects.get(pk=id)

        if subject and description:
            new_forum = Forum(subject=subject, description=description, user=user, book=book)
            new_forum.save()
            return HttpResponse(b"CREATED", status=201)
        else:
            return HttpResponseNotFound

    return HttpResponseNotFound()

@csrf_exempt
def add_reply_ajax(request,bookid,id):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        message = data.get("message").strip()
        user = request.user
        book = Book.objects.get(pk=bookid)
        forum = Forum.objects.get(pk=id)
        
        forum.total_reply +=1 
        forum.save()
        
        if message:
            new_reply = Reply(message=message, user=user, forum=forum)
            new_reply.save()
            return HttpResponse(b"CREATED", status=201)
        else:
            return HttpResponseNotFound()

    return HttpResponseNotFound()

@csrf_exempt
def create_forum_flutter(request,id):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.get(pk=id)

        new_forum = Forum.objects.create(
            user=request.user,
            subject=data["subject"],
            description=data["description"],
            book = book,
        )
        new_forum.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def create_reply_flutter(request,bookid,id):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.get(pk=bookid)
        forum = Forum.objects.get(pk=id)
        forum.total_reply +=1 
        forum.save()

        new_reply = Reply.objects.create(
            user=request.user,
            message=data["message"],
            forum=forum,
        )
        new_reply.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)