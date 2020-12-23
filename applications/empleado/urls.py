from django.urls import path

from . import views

app_name = "Empleado_App"

urlpatterns = [
    path('', views.IndexEmpleadoView.as_view(), name="Index"),
    # List
    path('ListaEmpleados/', views.ListAllEmpleados.as_view(), name="TodosLosEmpleados"),
    path('ListaEmpleadosPorArea/<NameDepto>/', views.ListEmpleadosByDepartamento.as_view(), name="EmpleadosPorArea"),
    path('VerEmpleado/<pk>/', views.EmpleadoDetailView.as_view(), name="DetalleEmpleado"),
    # Operations CRUD
    path('success/', views.successEmpleado.as_view(), name='Correcto'),
    path('RegistrarEmpleado/', views.AddEmpleadoCreateView.as_view(), name="RegistrarEmpleado"),
    path('ActualizarEmpleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='ActualizarEmpleado'),
    path('BorrarEmpleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='BorrarEmpleado'),

]
