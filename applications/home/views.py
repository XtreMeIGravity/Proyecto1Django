from django.shortcuts import render

# Create your views here.

# Generic Views
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)
# Import models
from .models import Prueba


class pruebaView(TemplateView):
    template_name = 'home/prueba.html'


class pruebaListView(ListView):
    template_name = "home/Lista.html"
    context_object_name = 'listaNumerosYPapas'
    queryset = ['papas',
                '1',
                '2']


class ListaPrueba(ListView):
    template_name = "home/lista_Prueba.html"
    model = Prueba
    context_object_name = 'Lista'


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    fields = [
        'titulo',
        'subtitulo',
        'cantidad',
    ]
