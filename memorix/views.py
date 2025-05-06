from django.shortcuts import render
from .models import Mazo, Tarjeta

def home(request):
    return render(request, "memorix/home.html")

def mis_mazos(request):
    mazos = Mazo.objects.all()
    return render(request, "memorix/mis_mazos.html", {"mazos": mazos})

def mis_tarjetas(request, mazo_id):
    mazo = Mazo.objects.get(id=mazo_id)
    tarjetas = mazo.tarjetas.all()
    return render(request, "memorix/mis_tarjetas.html", {"mazo": mazo, "tarjetas": tarjetas})