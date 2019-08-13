from django.shortcuts import render
from .models import Book


def date_stringify(date):
    return f'{date.year}-{date.month}-{date.day}'


def books_view(request, date_str=None):
    template = 'books/books_list.html'
    books = Book.objects.order_by('pub_date')
    book_values = list(books.values())
    book_obj = None

    context = {
        'books': []
    }

    for book in book_values:
        pub_date = book['pub_date']
        pub_date_string = date_stringify(pub_date)

        if date_str and date_str != pub_date_string:
            continue

        book_obj = book
        context['books'].append({
            'name': book['name'],
            'author': book['author'],
            'pub_date': pub_date_string
        })

    if date_str:
        def get_prev_date(ind):
            if ind - 1 >= 0:
                if book_obj['pub_date'] == book_values[ind - 1]['pub_date']:
                    get_prev_date(ind - 1)
                else:
                    result_date = book_values[ind - 1]['pub_date']
                    print(result_date)
                    return result_date  # не понимаю по какой причине тут возвращается None,
                    # хотя в print дата выводится. Хотел проверять рекурсивно, так как с одинаковыми датами выходит
                    # проблема - пагинация перестает работать
            else:
                return None

        index = book_values.index(book_obj)
        # prev_date = get_prev_date(index)
        # print(prev_date)  # Пришлось пока закомментировать

        if index - 1 >= 0:
            prev_date = date_stringify(book_values[index - 1]['pub_date'])
        else:
            prev_date = None

        if index + 1 <= (len(book_values) - 1):
            next_date = date_stringify(book_values[index + 1]['pub_date'])
        else:
            next_date = None

        context['dates'] = {
            'next': next_date,
            'prev': prev_date
        }

    return render(request, template, context)
