from django.db import models

# Create your models here.
from author.models import Author

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    available_copies = models.IntegerField(default=0)