import datetime
import os

from django.shortcuts import render
from app.settings import FILES_PATH


def file_list(request, date=None):
    template_name = 'index.html'
    context = {
        'files': []
    }
    files_list = os.listdir(FILES_PATH)

    if date:
        date = date.strip()
        try:
            new_date = datetime.datetime.strptime(date, '%Y-%m-%d')
            context['date'] = str(new_date.date())
        except Exception as e:  # Вот тут всё время вылетает ошибка, не пойму почему
            print(e)

    for file in files_list:
        c = round(os.stat(os.path.join(FILES_PATH, file)).st_ctime)
        m = round(os.stat(os.path.join(FILES_PATH, file)).st_mtime)

        try:
            if context['date'] != str(datetime.datetime.fromtimestamp(c).date()):
                continue
        except KeyError:
            pass

        context['files'].append({
            'name': file,
            'ctime': {
                'date': str(datetime.datetime.fromtimestamp(c).date()),
                'time': str(datetime.datetime.fromtimestamp(c).time())
            },
            'mtime': {
                'date': str(datetime.datetime.fromtimestamp(m).date()),
                'time': str(datetime.datetime.fromtimestamp(m).time())
            },
        })

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    try:
        file = os.path.join(FILES_PATH, name)
        with open(file) as f:
            s = f.read()
            return render(request, 'file_content.html', context={
                    'file_name': name,
                    'file_content': s
                }
            )
    except FileNotFoundError:
        return render(request, 'file_content.html', context={
                'file_name': 'Такого файла не существует',
                'file_content': 'Сорямба!'
            }
        )






