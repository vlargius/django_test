from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Mark


def index(request):
    return HttpResponse("test ok")


class IndexView(generic.ListView):
    template_name = 'marks/index.html'
    context_object_name = 'marks_list'

    def get_queryset(self):
        """Return the list of marks"""
        return Mark.objects

