from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


class StudentListView(ListView):
    model = Student
    ordering = 'group'
    queryset = Student.objects.all().prefetch_related('teacher')