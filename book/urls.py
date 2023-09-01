from django.urls import path
from book.views import home, add_wishlist, wishlist, add_borrowlist, borrowlist

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:book_id>/', add_wishlist, name='add_wishlist'),
    path('wishlist/', wishlist, name='wishlist'),
    path('borrow_book/<int:book_id>/', add_borrowlist, name='add_borrowlist'),
    path('borrowlist/', borrowlist, name='borrowlist'),
]
