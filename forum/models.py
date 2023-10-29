from django.db import models
from book.models import Book
from django.contrib.auth.models import User

class Forum(models.Model):
    subject = models.CharField(max_length=255, default='')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=True, null = True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    total_reply = models.IntegerField(default=0)

class Reply(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    