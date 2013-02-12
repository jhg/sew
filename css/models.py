from django.db import models


class HojaCss(models.Model):
    nombre = models.CharField(max_length=32, unique=True, blank=False)

    def __str__(self):
        return self.nombre

class SelectorCss(models.Model):
    valor = models.CharField(max_length=32, unique=False, blank=False)
    hojaCss = models.ManyToManyField(HojaCss)

    def __str__(self):
        return self.valor

class DeclaracionCss(models.Model):
    propiedad = models.CharField(max_length=32, unique=False, blank=False)
    valor = models.CharField(max_length=64, unique=False, blank=False)
    selectorCss = models.ManyToManyField(SelectorCss)

    def __str__(self):
        return self.propiedad
