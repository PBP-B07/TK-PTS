# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class BookEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE)
