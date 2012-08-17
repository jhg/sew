from django.db import models

UNIDADES_CHOICES = (
    ('u', 'u'),
    ('kg', 'kg'),
    ('g', 'g'),
    ('mg', 'mg'),
    ('l', 'l'),
    ('cl', 'cl'),
    ('ml', 'ml'),
)

class Receta(models.Model):
    nombre = models.CharField(max_length=64, default="", blank=False)
    descripcion = models.TextField(max_length=512, default="", blank=True)
    tiempo_elaboracion = models.TimeField(default="00:15:00")
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.nombre

class IngredienteReceta(models.Model):
    receta = models.ForeignKey(Receta)
    nombre = models.CharField(max_length=64, default="", blank=False)
    cantidad = models.DecimalField(max_digits=7,decimal_places=3)
    unidad = models.CharField(max_length=2,choices=UNIDADES_CHOICES)
    detalles = models.TextField(max_length=256, default="", blank=True)
    def __unicode__(self):
        return self.nombre

class PasoElaboracionReceta(models.Model):
    receta = models.ForeignKey(Receta)
    numero_paso = models.PositiveSmallIntegerField(blank=False)
    descripcion = models.TextField(max_length=1024, default="", blank=False)
    def __unicode__(self):
        return self.descripcion
