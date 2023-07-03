from django import forms
from .models import Producto


"""
{
    'id': 2,
    'nombre': 'Foco Subaru Impresa',
    'precio': 30000,
    'img': 'repuestos/ARR_foco.JPEG',
    'descripcion': None,
    'texto': None,
    'stock': 6,
    'categoria': 4,
    'estado': None
}
"""

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre',
            'precio',
            'categoria',
            'estado'
        )
        widgets = {
            'id'        : forms.HiddenInput(),
            'nombre'    : forms.HiddenInput(),
            'precio'    : forms.HiddenInput(),
            'categoria' : forms.HiddenInput(),
            'estado'    : forms.HiddenInput()
        }
