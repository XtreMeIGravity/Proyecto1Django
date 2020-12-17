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
from .forms import PruebaForm


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
    form_class = PruebaForm
    # Import Form
    success_url = '/'


# Template view
# Normal
class pruebaView(TemplateView):
    template_name = 'home/prueba.html'


# HEADER
class HeaderView(TemplateView):
    template_name = "home/conmon/header.html"


# FOOTER
class FooterView(TemplateView):
    template_name = "home/conmon/Footer.html"
