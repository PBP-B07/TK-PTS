from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class UlasanBuatan(models.Model):
    rate = models.IntegerField()
    description = models.TextField()

class ForumBuatan(models.Model):
    rate = models.IntegerField()
    description = models.TextField()

class BukuBuatan(models.Model):
    rate = models.IntegerField()
    description = models.TextField()