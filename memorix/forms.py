from django import forms
from .models import Tarjeta, Mazo

class MazoForm(forms.ModelForm):
    class Meta:
        model = Mazo
        fields = ["nombre"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "input", "placeholder": "Ingrese el nombre del mazo"}),
        }

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ["anverso", "reverso"]
        widgets = {
            "anverso": forms.TextInput(attrs={"class": "input", "placeholder": "Ingrese el anverso"}),
            "reverso": forms.TextInput(attrs={"class": "input", "placeholder": "Ingrese el reverso"}),
        }
