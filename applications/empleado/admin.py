from django.contrib import admin

from .models import Empleado, Habilidad

# Register your models here.

admin.site.register(Habilidad)


class EmpleadoAdmin(admin.ModelAdmin):
    search_fields = [
        'firts_name',
        'last_name',
    ]

    list_filter = (
        'departamento',
        'job',
        'habilidades',
    )

    filter_horizontal = (
        'habilidades',
    )

    list_display = (
        'id',
        'firts_name',
        'last_name',
        'departamento',
        'job',
        'full_name',  # Concat
    )

    @staticmethod
    def full_name(obj):
        return obj.firts_name + ' ' + obj.last_name


admin.site.register(Empleado, EmpleadoAdmin)
