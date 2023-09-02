from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

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
    
    def __str__(self):
        return self.title
    
class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item.title
    
class BorrowList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField()
    return_date = models.DateTimeField(default=datetime.now() + timedelta(days = 15))
    
    def __str__(self):
        return self.item.title