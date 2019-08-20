from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Product, Review
from .forms import ReviewForm


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductView(DetailView):
    model = Product
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['reviews'] = Review.objects.filter(product=self.object)

        if self.object.id in self.request.session.get('reviewed_products', []):
            context['is_review_exist'] = True
            return context

        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        product_id = self.kwargs['pk']

        if form.is_valid():
            review = form.save(commit=False)
            review.product_id = product_id
            review.save()

            reviewed_products = self.request.session.get('reviewed_products', [])
            reviewed_products.append(product_id)
            self.request.session['reviewed_products'] = reviewed_products

        return redirect(reverse('product_detail', kwargs=self.kwargs))
