from django.db import models

# Create your models here.
from django.db import models

class BookEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    book_related = models.BooleanField(default=True)  # Menyatakan bahwa event ini berhubungan dengan buku

    def __str__(self):
        return self.title
