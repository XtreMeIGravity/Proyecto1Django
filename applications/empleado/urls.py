from django.urls import path

from . import views

app_name = "Empleado_App"

urlpatterns = [
    path('', views.IndexEmpleadoView.as_view(), name="Index"),
    path('ListaEmpleadosDepto/<nameArea>/', views.ListByArea.as_view()),
    path('ListaEmpleadosKeyword/', views.ListByKeyword.as_view()),
    path('ListaEmpleadosHabilidades/', views.ListByHabilidades.as_view()),
    path('ListaEmpleadosJob/', views.ListByJob.as_view()),
    # Lista
    path('ListaEmpleados/', views.ListAllEmpleados.as_view(), name="TodosLosEmpleados"),
    path('VerEmpleado/<pk>/', views.EmpleadoDetailView.as_view(), name="DetalleEmpleado"),
    # Operations CRUD
    path('success/', views.successEmpleado.as_view(), name='Correcto'),
    path('RegistrarEmpleado/', views.AddEmpleadoCreateView.as_view()),
    path('ActualizarEmpleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='ActualizarEmpleado'),
    path('BorrarEmpleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='BorradoCorrectamente'),

]
