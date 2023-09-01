from django.shortcuts import render
from book.models import Book

# Create your views here.
def home(request):
    query = request.GET.get('search')
    if query:
        books = Book.objects.filter(title__icontains = query)
    else:
        books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)