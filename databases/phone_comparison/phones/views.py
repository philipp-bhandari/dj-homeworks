from django.shortcuts import render
from .models import Phone, LG, Huawei


def show_catalog(request):
    lg_phone = LG.objects.first()
    h_phone = Huawei.objects.first()
    context = {
        'phones': []
    }
    for mob in [lg_phone, h_phone]:
        phone = {
            'model': f'{mob.__class__.__name__} {mob.model}',
            'price': mob.phone.price,
            'os': mob.phone.os_sys,
            'resolution': mob.phone.resolution,
            'matrix': mob.phone.cam_matrix,
            'ram': mob.phone.ram_memory,
            'fm': mob.fm_radio,
            'ir': mob.ir_port
        }
        context['phones'].append(phone)
        context['field_names'] = [
            'Модель', 'Цена', 'ОС', 'Разрешение', 'Камера', 'Память', 'Радио', 'ИК-порт'
        ]

    template = 'catalog.html'

    return render(
        request,
        template,
        context
    )
