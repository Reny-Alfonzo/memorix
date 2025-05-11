from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("mazos/<int:mazo_id>/", views.mis_tarjetas, name="mis_tarjetas"),
    path("crear_mazo/", views.crear_mazo, name="crear_mazo"),
    path("mazos/", views.mis_mazos, name="mis_mazos"),
    path("mazos/<int:mazo_id>/agregar_tarjeta/", views.agregar_tarjeta, name="agregar_tarjeta")
]