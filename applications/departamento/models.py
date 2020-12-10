from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('nombre',max_length=50, unique=True)
    short_name = models.CharField('nombre_corto', max_length=20, blank=True, unique=True)
    anulate = models.BooleanField('anulado',default=False)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['short_name']
        unique_together = ('name', 'short_name')

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' ' + self.short_name
