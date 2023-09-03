from django.urls import path
from book.views import home, add_wishlist, wishlist, add_borrowlist, borrowlist, return_book

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:book_id>/', add_wishlist, name='add_wishlist'),
    path('wishlist/', wishlist, name='wishlist'),
    path('borrow_book/<int:book_id>/', add_borrowlist, name='add_borrowlist'),
    path('borrowlist/', borrowlist, name='borrowlist'),
    path('return_book/<int:book_id>/', return_book, name='return_book'),
]
