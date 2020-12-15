from django import forms

from .models import Prueba


class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = [
            'titulo',
            'subtitulo',
            'cantidad',
        ]
        widgets = {
            'cantidad': forms.TextInput(
                attrs={
                    'placeholder': 'ingrese la cantidad'
                }
            ),
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'ingrese el titulo'
                }
            ),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if (cantidad < 10):
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad
