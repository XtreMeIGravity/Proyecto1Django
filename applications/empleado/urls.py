from django.urls import path

from . import views

urlpatterns = [
    path('ListaEmpleados/', views.ListAllEmpleados.as_view()),
    path('ListaEmpleadosDepto/<nameArea>/', views.ListByArea.as_view()),
    path('ListaEmpleadosKeyword/', views.ListByKeyword.as_view()),
    path('ListaEmpleadosHabilidades/', views.ListByHabilidades.as_view()),
    path('ListaEmpleadosJob/', views.ListByJob.as_view()),

]
