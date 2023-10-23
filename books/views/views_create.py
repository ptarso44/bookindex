from django.views.generic import CreateView
from books.models import Book


class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author', 'publisher', 'release_date']
