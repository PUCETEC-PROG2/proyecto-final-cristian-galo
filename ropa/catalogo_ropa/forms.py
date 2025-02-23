from django import forms
from django.utils import timezone
from .models import *
from django.forms.widgets import DateInput, CheckboxSelectMultiple

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'talla': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}), 
            'imagen' : forms.ClearableFileInput(attrs={'class': 'form-control', 'required': 'required'}),

        }



class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'fecha_compra': DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'productos': CheckboxSelectMultiple(attrs={'class': 'form-check-label'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'cliente': 'Cliente',
            'fecha_compra': 'Fecha de la Compra',
            'productos': 'Productos',
            'ciudad': 'Ciudad',
            'precio_total' : 'Precio total'
        }

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.fields['fecha_compra'].initial = timezone.now().date()
        self.fields['productos'].queryset = Producto.objects.all()



class CompraDetailForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
        widgets = {
            'cliente': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'fecha_compra': forms.DateInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'productos': forms.SelectMultiple(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'precio_total': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
        }
        labels = {
            'cliente': 'Id del Cliente',
            'fecha_compra': 'Fecha de la Compra',
            'productos': 'Productos',
            'ciudad': 'Ciudad',
            'precio_total' : 'Precio total'
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
           'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
           'apellidos' : forms.TextInput(attrs={'class' : 'form-control'}),
           'cedula' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'telefono' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'correo' : forms.EmailInput(attrs={'class' : 'form-control'}),
        }
