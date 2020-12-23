from django.urls import path

from . import views

app_name = "Departamento_App"

urlpatterns = [
    path('NuevoDepartamento/', views.NewDepartamentoView.as_view(), name='NuevoDepartamento'),
    path('ListaDepartamentos/', views.DepartamentoListView.as_view(), name='TodosLosDepartamentos'),
    path('DetalleDepartamento/<pk>/', views.DepartamentoListView.as_view(), name='DetalleDepartamento'),
]
