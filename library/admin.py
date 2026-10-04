from django.contrib import admin

from .models import Book
@admin.register(Book)
class book(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'price', 'author']