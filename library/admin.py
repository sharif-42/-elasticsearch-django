from django.contrib import admin

from .models import Author, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'author', 'isbn']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'first_name', 'email', ]
