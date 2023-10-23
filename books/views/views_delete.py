from django.views.generic import DeleteView
from books.models import Book


class BookDeleteView(DeleteView):
    model = Book
    fields = ['name', 'author', 'publisher', 'release_date']