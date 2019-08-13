from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    context = {
        'phones': []
    }

    sort = request.GET.get('sort')
    if sort in ['name', 'price', '-price']:
        phones = Phone.objects.order_by(sort)
    else:
        phones = Phone.objects.all()

    for phone in phones:
        context['phones'].append({
            'name': phone.name,
            'price': phone.price,
            'image': phone.image,
            'link': f'/catalog/{phone.slug}/'
        })

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone = Phone.objects.get(slug=slug)
    except:
        return render(request, template, {'phone': { 'name': 'Такой страницы нет' }})
    context = {
        'phone': {
            'name': phone.name,
            'image': phone.image,
            'price': phone.price,
            'release_date': phone.release_date,
            'lte_exists': phone.lte_exists
        }
    }
    return render(request, template, context)