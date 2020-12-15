from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic.edit import FormView

# Formularios
from .forms import NewDepartamentoForm

# Modelos
from applications.empleado.models import Empleado
from .models import Departamento


# Create your views here.

class NewDepartamentoView(FormView):
    template_name = "departamento/NewDepartamento.html"
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        # Logic Process
        nombre_Empleado = form.cleaned_data['nombre_Empleado']
        apellidos_Empleado = form.cleaned_data['apellidos_Empleado']

        depto = Departamento(
            name=form.cleaned_data['nombre_Departamento'],
            short_name=form.cleaned_data['ShorName_Departamento']
        )
        depto.save()

        Empleado.objects.create(
            firts_name=nombre_Empleado,
            last_name=apellidos_Empleado,
            job='1',
            departamento=depto
        )

        return super(NewDepartamentoView, self).form_valid(form)
