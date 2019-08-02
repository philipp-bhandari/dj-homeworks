from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from app.settings import BUS_STATION_CSV
import csv
import math


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    try:
        num = int(request.GET.get('page'))
    except TypeError:
        num = 1

    if num > 1:
        prev_page = f'?page={num - 1}'
    else:
        prev_page = None

    context_dict = {
        'bus_stations': [],
        'current_page': num,
        'prev_page_url': prev_page,
    }
    next_page = None
    rows_on_page = 10

    with open(BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        enum_reader = enumerate(reader)
        page_count = 99999
        # Не получается таким образом посчитать количество страниц, если раскомментировать строчку
        # list_reader = list(reader), то последний цикл for не работает, я не могу понять почему.

        # list_reader = list(reader)  # <---------------------------------------------- ?!
        # page_count = math.ceil(len(list_reader) / rows_on_page)

        if num > page_count:
            return render_to_response('index.html', context={
                'bus_stations': [{'Name': 'Такой', 'Street': 'страницы', 'District': 'нет'}],
                'current_page': num,
                'prev_page_url': f'?page={page_count}',
                'next_page_url': next_page,
            })
        else:
            next_page = f'?page={num + 1}'
        context_dict['next_page_url'] = next_page

        for i, row in enum_reader:
            if num * rows_on_page < i:
                break
            if num * rows_on_page - rows_on_page <= i:
                bus_stop = {
                    'Name': row['Name'],
                    'Street': row['Street'],
                    'District': row['District']
                }
                context_dict['bus_stations'].append(bus_stop)
    return render_to_response('index.html', context=context_dict)




