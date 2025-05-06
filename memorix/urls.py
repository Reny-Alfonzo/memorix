from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("mazos/", views.mis_mazos, name="mis_mazos"),
    path("mazos/<int:mazo_id>/", views.mis_tarjetas, name="mis_tarjetas"),
]