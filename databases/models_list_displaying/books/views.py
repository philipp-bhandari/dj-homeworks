from django.shortcuts import render
from .models import Book
from datetime import date


def date_stringify(date):
    return f'{date.year}-{date.month}-{date.day}'


def add_to_context(values, context):
    for book in values:
        pub_date = book['pub_date']
        pub_date_string = date_stringify(pub_date)
        context['books'].append({
            'name': book['name'],
            'author': book['author'],
            'pub_date': pub_date_string
        })
    return context


def books_view(request, date_str=None):
    template = 'books/books_list.html'
    context = {
        'books': []
    }

    if date_str:
        books = Book.objects.filter(pub_date=date_str)
        book_values = list(books.values())
        context = add_to_context(book_values, context)

        prev_book = Book.objects.filter(pub_date__lt=date_str).first()
        next_book = Book.objects.filter(pub_date__gt=date_str).order_by('pub_date').first()

        if prev_book:
            prev = date_stringify(prev_book.pub_date)
        else:
            prev = None
        if next_book:
            next = date_stringify(next_book.pub_date)
        else:
            next = None

        context['dates'] = {
            'prev': prev,
            'next': next
        }
    else:
        books = Book.objects.order_by('pub_date')
        book_values = list(books.values())
        context = add_to_context(book_values, context)

    return render(request, template, context)


