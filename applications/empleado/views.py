from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    ListView,
)

# Models
from .models import Empleado


class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    model = Empleado
    context_object_name = 'listaEmpleados'
    paginate_by = 5
    ordering = 'firts_name'


class ListByArea(ListView):
    template_name = 'empleado/list_depto.html'
    context_object_name = 'ListaPorDepartamento'

    def get_queryset(self):
        area = self.kwargs['nameArea']
        lista = Empleado.objects.filter(
            departamento__name=area
        )
        return lista


class ListByKeyword(ListView):
    template_name = "empleado/list_keyword.html"
    context_object_name = "ListaEmpleadoPorTrabajo"

    def get_queryset(self):
        palabra_buscar = self.request.GET.get('Buscador', '')
        Lista = Empleado.objects.filter(
            firts_name=palabra_buscar
        )
        return Lista


class ListByJob(ListView):
    template_name = "empleado/list_job.html"
    context_object_name = "ListaPorTrabajo"

    def get_queryset(self):
        trabajo = self.request.GET.get('Buscador', '')
        ListaxD = Empleado.objects.all()
        for x in ListaxD:
            print(x.job.get_job_display() )
        return ListaxD


class ListByHabilidades(ListView):
    template_name = "empleado/List_Habilidades.html"
    context_object_name = "ListaPorHabilidades"

    def get_queryset(self):
        empleado = Empleado.objects.get(id=2)
        print(empleado.habilidades.all())
        return []