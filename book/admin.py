from django.contrib import admin
from book.models import Book, WishList, BorrowList

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'publication_date', 'genre', 'book_no', 'is_available']
    
class BorrowListAdmin(admin.ModelAdmin):
    list_display = ['item', 'user', 'borrow_date', 'return_date', 'fine']

admin.site.register(Book, BookAdmin)
admin.site.register(BorrowList, BorrowListAdmin)
admin.site.register(WishList)