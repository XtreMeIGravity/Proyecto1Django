from django.urls import path

from . import views

app_name = "Empleado_App"

urlpatterns = [
    path('ListaEmpleados/', views.ListAllEmpleados.as_view()),
    path('ListaEmpleadosDepto/<nameArea>/', views.ListByArea.as_view()),
    path('ListaEmpleadosKeyword/', views.ListByKeyword.as_view()),
    path('ListaEmpleadosHabilidades/', views.ListByHabilidades.as_view()),
    path('ListaEmpleadosJob/', views.ListByJob.as_view()),
    path('VerEmpleado/<pk>/', views.EmpleadoDetailView.as_view()),
    path('RegistrarEmpleado/', views.AddEmpleadoCreateView.as_view()),
    path('success/', views.successEmpleado.as_view(), name='RegistroCorrecto'),

]
