from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    ordering = ('-pk',)
    list_filter = ('brand',)
    search_fields = ['brand', 'model']
    list_display = ('brand', 'model', 'review_count')


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    ordering = ('-pk',)
    list_filter = ('car', 'title')
    search_fields = ['car__model', 'car__brand', 'title']


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
