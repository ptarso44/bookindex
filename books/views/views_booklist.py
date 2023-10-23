from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book


def booklist(request):

    books = Book.objects.all().order_by('name')

    items_per_page = int(request.GET.get('pagesize', 4))
    books_paginator = Paginator(books, items_per_page)

    total_pages = books_paginator.num_pages
    page_number = request.GET.get('page', 1)
    book_items = books_paginator.get_page(page_number)
    current_page = book_items.number
    boundaries = 2
    around = 2

    page_numbers = books_paginator.get_elided_page_range(page_number, on_each_side=boundaries, on_ends=around)

    page_title = 'Book List - Books Index'

    context = {
        'title': page_title,
        'current_page': current_page,
        'total_pages': total_pages,
        'page_numbers': page_numbers,
        'current_page_items': book_items,
    }

    return render(request, 'books/book_list.html', context)
