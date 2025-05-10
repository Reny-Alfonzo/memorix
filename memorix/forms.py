from django import forms
from .models import Tarjeta, Mazo



class MazoForm(forms.ModelForm):
    class Meta:
        model = Mazo
        fields = ["nombre"]

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ["nombre", "mazo", "anverso", "reverso"]

