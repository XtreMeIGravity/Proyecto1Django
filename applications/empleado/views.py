from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

# Models
from .models import Empleado


class IndexEmpleadoView(TemplateView):
    """vista que carga la pagina de inicio"""
    template_name = "IndexEmpleado.html"


# GRID DATA
class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    model = Empleado
    context_object_name = 'listaEmpleados'
    ordering = 'firts_name'
    paginate_by = 5

    def get_queryset(self):
        busqueda = self.request.GET.get('keyword', '')
        lista = Empleado.objects.filter(
            firts_name__icontains=busqueda,
        )
        return lista


# Detail View
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/EmpleadoDetailView.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        ListaChoice = Empleado.Job_Choices
        res = [n[1] for n in ListaChoice if n[0] == self.object.job]
        context['name_job'] = res[0]
        return context


# Success Message
class successEmpleado(TemplateView):
    template_name = "empleado/success.html"


# add view
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
    success_url = reverse_lazy('Empleado_App:Correcto')

    def form_valid(self, form):
        # Logic Process
        empleado = form.save()
        empleado.full_name = empleado.firts_name + ' ' + empleado.last_name
        empleado.save()
        return super(AddEmpleadoCreateView, self).form_valid(form)


class successUpdateEmpleado(TemplateView):
    template_name = "empleado/sucessUpdate.html"


# update view
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/UpdateEmpleado.html"
    fields = [
        'firts_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'hoja_vida',
    ]
    success_url = reverse_lazy('Empleado_App:Correcto')

    # Intercept values of POST
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Logic Process
        empleado = form.save()
        empleado.full_name = empleado.firts_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)


# delete view
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/DeleteEmpleado.html"
    success_url = reverse_lazy('Empleado_App:Correcto')
