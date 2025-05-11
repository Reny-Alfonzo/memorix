from django.urls import path
from . import views

urlpatterns = [
    path("mazos/<int:mazo_id>/estudiar/", views.estudiar_mazo, name="estudiar_mazo"),
]
