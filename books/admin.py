from django.contrib import admin
from .models import Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'publication_date', 'status')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'publisher')
    ordering = ('status', 'created_at')

admin.site.register(Book, BookAdmin)