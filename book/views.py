from django.shortcuts import render, redirect
from book.models import Book, WishList

# Create your views here.
def home(request):
    query = request.GET.get('search')
    if query:
        books = Book.objects.filter(title__icontains = query)
    else:
        books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)

def add_wishlist(request, book_id):
    book = Book.objects.get(id = book_id)
    item = WishList.objects.create(
        user = request.user,
        item = book,
    )
    item.save()
    
    return redirect('home')

def wishlist(request):
    wishlist = WishList.objects.filter(user = request.user)
    return render(request, 'wishlist.html', {'books': wishlist})