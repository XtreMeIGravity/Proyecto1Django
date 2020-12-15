from django import forms

from applications.empleado.models import Empleado


class NewDepartamentoForm(forms.Form):
    nombre_Empleado = forms.CharField(max_length=50)
    apellidos_Empleado = forms.CharField(max_length=50)
    nombre_Departamento = forms.CharField(max_length=50)
    ShorName_Departamento = forms.CharField(max_length=50)
