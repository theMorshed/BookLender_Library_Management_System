from django.shortcuts import render, redirect
from book.models import Book, WishList, BorrowList
from datetime import datetime, timedelta

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
    if not request.user.is_authenticated:
        return redirect('login')
    
    book = Book.objects.get(id = book_id)
    is_exists = WishList.objects.filter(item = book, user = request.user)
    if not is_exists:
        item = WishList.objects.create(
            user = request.user,
            item = book,
        )
        item.save()
    
    return redirect('wishlist')

def wishlist(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    wishlist = WishList.objects.filter(user = request.user)
    return render(request, 'wishlist.html', {'books': wishlist})

def add_borrowlist(request, book_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    book = Book.objects.get(id = book_id)
    is_exists = BorrowList.objects.filter(item = book, user = request.user)
    if not is_exists:
        item = BorrowList.objects.create(
            user = request.user,
            item = book,
            borrow_date = datetime.now(),
            return_date = datetime.now() + timedelta(days = 15),
        )
        item.save()
    return redirect('borrowlist')

def borrowlist(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    borrowlist = BorrowList.objects.filter(user = request.user)
    return render(request, 'borrowlist.html', {'books': borrowlist})