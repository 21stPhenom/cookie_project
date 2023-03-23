import hashlib

from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    name = models.CharField(verbose_name='Book name', max_length=500)
    author = models.CharField(verbose_name='Book author', max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)
    book_hash = models.CharField(verbose_name='Book Hash', max_length=10, blank=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return f"'{self.name}' by '{self.author}'"
