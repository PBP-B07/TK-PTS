from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user_profile.models import User
from books.models import Books

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    description = models.CharField(max_length=254)
    star = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    date_added = models.DateField(auto_now_add=True)