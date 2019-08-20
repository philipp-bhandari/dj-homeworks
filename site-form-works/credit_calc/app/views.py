from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"

    def get(self, request, *args, **kwargs):
        form = CalcForm(request.GET)
        result, common_result = None, None

        if form.is_valid():
            data = form.cleaned_data
            common_result = int(data['initial_fee'] + data['initial_fee'] * data['rate'] / 100)
            result = int(common_result / data['months_count'])

        context = {
            'form': form,
            'result': result,
            'common_result': common_result
        }

        return render(request, self.template_name, context)
