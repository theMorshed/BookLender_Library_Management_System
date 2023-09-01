from django.shortcuts import render, redirect
from book.models import Book, WishList, BorrowList
from datetime import datetime

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

def add_borrowlist(request, book_id):
    book = Book.objects.get(id = book_id)
    item = BorrowList.objects.create(
        user = request.user,
        item = book,
        borrow_date = datetime.now(),
    )
    item.save()
    
    return redirect('home')

def borrowlist(request):
    borrowlist = BorrowList.objects.filter(user = request.user)
    return render(request, 'borrowlist.html', {'books': borrowlist})