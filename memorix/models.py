from django.db import models

class Mazo(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre

class Tarjeta(models.Model):
    mazo = models.ForeignKey(Mazo, on_delete=models.CASCADE, related_name="tarjetas")
    nombre = models.CharField(max_length=255)
    anverso = models.TextField()
    reverso = models.TextField()

    def __str__(self):
        return self.nombre