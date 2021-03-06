from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField


# Create your models here.


class Habilidad(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    
    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.habilidad


class Empleado(models.Model):

    Job_Choices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )

    firts_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField('Nombre Completo', max_length=100, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=Job_Choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    # Relation many to many
    habilidades = models.ManyToManyField(Habilidad)
    hoja_vida = RichTextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['id', 'last_name', 'firts_name']
        unique_together = ('last_name', 'firts_name')

    def __str__(self):
        return self.firts_name +' - '+ self.last_name +' - '+ self.job +' - '+self.get_job_display()