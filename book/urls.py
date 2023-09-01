from django.urls import path
from book.views import home, add_wishlist, wishlist

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:book_id>/', add_wishlist, name='add_wishlist'),
    path('wishlist/', wishlist, name='wishlist'),
]
