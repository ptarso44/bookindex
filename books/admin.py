from django.contrib import admin
from .models import Book


admin.site.empty_value_display = "(None)"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'
    list_display = ['name', 'author', 'publisher', 'release_date']
    ordering = ['name', 'author', 'publisher', '-release_date']
