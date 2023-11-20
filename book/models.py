from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    isbn10 = models.TextField(null=True, blank=True)
    isbn13 = models.TextField(null=True, blank=True)
    publish_date = models.TextField(null=True, blank=True)
    edition = models.IntegerField(null=True, blank=True)
    best_seller = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)