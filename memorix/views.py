from django.shortcuts import render, redirect
from .models import Mazo
from .forms import MazoForm, TarjetaForm

def home(request):
    return render(request, "memorix/home.html")

def crear_mazo(request):
    if request.method == "POST":
        form = MazoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agregar_tarjeta", mazo_id=form.instance.id)  # Redirigir a agregar tarjeta
    else:
        form = MazoForm()
    return render(request, "memorix/crear_mazo.html", {"form": form})

def mis_mazos(request):
    mazos = Mazo.objects.prefetch_related("tarjetas").all()  # Mejora el rendimiento
    return render(request, "memorix/mis_mazos.html", {"mazos": mazos})

def mis_tarjetas(request, mazo_id):
    mazo = Mazo.objects.select_related().get(id=mazo_id)
    tarjetas = mazo.tarjetas.all()
    return render(request, "memorix/mis_tarjetas.html", {"mazo": mazo, "tarjetas": tarjetas})

def agregar_tarjeta(request, mazo_id):
    mazo = Mazo.objects.get(id=mazo_id)

    if request.method == "POST":
        form = TarjetaForm(request.POST)
        if form.is_valid():
            tarjeta = form.save(commit=False)
            tarjeta.mazo = mazo  # Asignar la tarjeta al mazo seleccionado
            tarjeta.save()
            return redirect("mis_tarjetas", mazo_id=mazo.id)
    else:
        form = TarjetaForm()

    return render(request, "memorix/agregar_tarjeta.html", {"form": form, "mazo": mazo})

