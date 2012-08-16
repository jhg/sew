from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=64, default="", blank=False)
    descripcion = models.TextField(max_length=512, default="", blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.nombre

class IngredienteReceta(models.Model):
    receta = models.ForeignKey(Receta)
    nombre = models.CharField(max_length=64, default="", blank=False)
    # cantidad
    # unidad
    detalles = models.TextField(max_length=256, default="", blank=True)
    def __unicode__(self):
        return self.nombre

class PasoElaboracionReceta(models.Model):
    receta = models.ForeignKey(Receta)
    # numero de paso en receta
    descripcion = models.TextField(max_length=1024, default="", blank=False)
    def __unicode__(self):
        return self.descripcion
