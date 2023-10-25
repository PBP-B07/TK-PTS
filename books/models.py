from django.db import models
# from django.contrib.auth.models import User

class Books(models.Model):
    title = models.TextField(null=True, blank=True),
    description = models.TextField(null=True, blank=True),
    author = models.TextField(null=True, blank=True),
    isbn10 = models.IntegerField(null=True, blank=True),
    isbn13 = models.TextField(null=True, blank=True),
    publish_date = models.TextField(null=True, blank=True),
    edition = models.IntegerField(null=True, blank=True),
    best_seller = models.TextField(null=True, blank=True),
    top_rated = models.TextField(null=True, blank=True),
    rating = models.FloatField(null=True, blank=True),
    review_count = models.IntegerField(null=True, blank=True),
    price = models.TextField(null=True, blank=True)
