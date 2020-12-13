from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
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
        ListaChoice = Empleado.Job_Choices
        trabajoSelect = [n[0] for n in ListaChoice if n[1] == trabajo]
        Lista = Empleado.objects.filter(
            job=trabajoSelect[0]
        )
        return Lista


class ListByHabilidades(ListView):
    template_name = "empleado/List_Habilidades.html"
    context_object_name = "ListaPorHabilidades"

    def get_queryset(self):
        empleado = Empleado.objects.get(id=2)
        print(empleado.habilidades.all())
        return []


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/EmpleadoDetailView.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'EmpleadoDelMes'
        return context


class successEmpleado(TemplateView):
    template_name = "empleado/success.html"


class AddEmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/AddEmpleado.html"
    # fields = ('__all__')
    fields = [
        'firts_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'hoja_vida',
    ]
    success_url = reverse_lazy('Empleado_App:RegistroCorrecto')

    def form_valid(self, form):
        # Logic Process
        empleado = form.save()
        empleado.full_name = empleado.firts_name+' '+empleado.last_name
        empleado.save()
        return super(AddEmpleadoCreateView, self).form_valid(form)

