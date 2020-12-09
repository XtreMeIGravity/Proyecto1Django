from django.db import models

from applications.departamento.models import Departamento


# Create your models here.

class Empleado(models.Model):

    Job_Choices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )

    firts_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=1, choices=Job_Choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    #

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return self.firts_name +' - '+ self.last_name
