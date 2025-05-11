from django.shortcuts import render
from memorix.models import Mazo, Tarjeta

def estudiar_mazo(request, mazo_id):
    mazo = Mazo.objects.get(id=mazo_id)
    tarjetas = mazo.tarjetas.all()
    return render(request, "estudio/estudiar_mazo.html", {"mazo": mazo, "tarjetas": tarjetas})
