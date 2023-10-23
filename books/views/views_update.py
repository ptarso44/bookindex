from django.views.generic import UpdateView
from books.models import Book


class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'author', 'publisher', 'release_date']