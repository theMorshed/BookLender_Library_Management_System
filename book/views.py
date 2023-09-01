from django.shortcuts import render
from book.models import Book

# Create your views here.
def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)