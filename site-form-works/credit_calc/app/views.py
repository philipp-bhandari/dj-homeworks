from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"

    form = CalcForm
    context = {}

    if request.GET.get('initial_fee') and request.GET.get('rate') and request.GET.get('months_count'):
        form = CalcForm(request.GET)
        if form.is_valid():
            fee = form.cleaned_data['initial_fee']
            rate = form.cleaned_data['rate']
            months = form.cleaned_data['months_count']
            summ = fee + fee * (rate / 100)
            for_month = summ / months
            context['result'] = {
                'summ': summ,
                'month': for_month
            }

    context['form'] = form

    return render(request, template, context)
