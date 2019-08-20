import time
import random

from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


class TicketPageView(FormMixin, TemplateView):
    form_class = SearchTicket
    template_name = 'app/ticket_page.html'


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    term = request.GET.get('term')

    cache_key = term.lower().replace(' ', '_')
    results = cache.get(cache_key)

    if results is None:
        results = list(City.objects.filter(name__contains=term.capitalize()).values_list('name', flat=True))
        cache.set(cache_key, results)

    return JsonResponse(results, safe=False)
