from django.contrib import admin
from book.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'publication_date', 'genre', 'book_no', 'is_available']
    
admin.site.register(Book, BookAdmin)