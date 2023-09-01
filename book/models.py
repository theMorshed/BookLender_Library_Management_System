from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_images')
    isbn = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100)
    book_no = models.IntegerField()
    is_available = models.BooleanField(default=True)