from unittest.util import _MAX_LENGTH
from django import forms
from django.db.models import fields
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, label="Nombre")
    description = forms.CharField(max_length=255, required=True, label="Descripcion")
    schedule = forms.CharField(max_length=255, required=True, label="Horario")
    contact = forms.CharField(max_length=12, required=True, label="Telefono")
    price = forms.CharField( required=True, label="Precio")

class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'schedule', 'contact', 'price', ]
        labels = {
            'name': 'Nombre',
            'description': 'Descripcion',
            'contact': 'Contacto',
            'price': 'Precio',
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'schedule', 'contact', 'price', ]
        labels = {
            'name': 'Nombre',
            'description': 'Descripcion',
            'contact': 'Contacto',
            'price': 'Precio',
        }