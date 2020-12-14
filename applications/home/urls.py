from django.contrib import admin
from django.urls import path


from . import views

app_name = "Home_App"

urlpatterns = [
    path('prueba/', views.pruebaView.as_view()),
    path('lista/', views.pruebaListView.as_view()),
    path('listaModel/', views.ListaPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='Add'),
]
