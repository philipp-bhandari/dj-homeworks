from django.shortcuts import render
import csv
import os


def inflation_view(request):
    template_name = 'inflation.html'
    context = {
        'data': []
    }
    with open(os.path.abspath('inflation_russia.csv'), newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')

        for i, row in enumerate(reader):
            data_list = []
            for k, td in enumerate(row):
                num = td
                if row[k] is row[-1]:
                    color = 'gray'
                elif row[k] is row[0]:
                    color = None
                else:
                    try:
                        num = float(td)
                        if num < 0:
                            color = 'green'
                        elif 1 <= num < 2:
                            color = 'lightsalmon'
                        elif 2 <= num < 5:
                            color = 'salmon'
                        elif num >= 5:
                            color = 'indianred'
                        else:
                            color = None
                    except:
                        color = None
                data = {
                    'color': color,
                    'data': num
                }
                data_list.append(data)
            context['data'].append(data_list)

    return render(request, template_name,
                  context=context)
