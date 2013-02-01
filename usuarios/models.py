from django.db import models


class TipoAutenticacion(models.Model):
    nombre = models.CharField(max_length=128, unique=True)

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
    es_anonimo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
