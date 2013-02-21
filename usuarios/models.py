from django.db import models
from importlib import import_module


class TipoAutenticacion(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    modulo = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=32, unique=True, blank=False)
    grupo = models.ManyToManyField(Grupo)
    tipo_de_autenticacion = models.ForeignKey(TipoAutenticacion)
    valor_de_autenticacion = models.CharField(max_length=512)

    def __str__(self):
        return self.nombre
