from django.urls import path

from . import views

urlpatterns = [
    path('NewDepartamento/', views.NewDepartamentoView.as_view(), name='nuevo_departamento'),
]
