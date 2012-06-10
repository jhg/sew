#-*- coding: UTF-8 -*-
from django.contrib.auth.models import User, Group
from settings_local import PROJECT_DIR
from django.db import models
from sew.slughifi import slughifi


# Abrimos el archivo de la plantilla predeterminada de los blogs
plantilla_predeterminada = open(PROJECT_DIR
                              +"/plantillas/blogs/plantilla_predeterminada.htm",
                              "r")
class Blog(models.Model):
    titulo = models.CharField(max_length=64, default="", blank=False)
    # Fragmento de URL que seguira a la url de blogs e identifica este blog
    url = models.SlugField(max_length=64, default="", unique=True, blank=False)
    publicado = models.BooleanField(default=False)
    bloqueado = models.BooleanField(default=False)
    descripcion = models.TextField(max_length=256, default="", blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    articulos_por_pagina = models.IntegerField(default=1, blank=False)
    accesos_directos_paginacion = models.IntegerField(default=3, blank=False)
    # Plantilla de 8KB
    plantilla = models.TextField(max_length=8192,
        default=plantilla_predeterminada.read(), # La plantilla predeterminada
        blank=True)
    # Autores (individuales) y colectivo de autores (todos los del grupo)
    autores = models.ManyToManyField(User, blank=True)
    colectivos = models.ManyToManyField(Group, blank=True)
    def save(self, *args, **kwargs):
        # NOTA: mejorar sistemas de URLs amigables
        self.url = slughifi(self.url)
        super(Blog, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.titulo
plantilla_predeterminada.close() # Cerramos el archivo

class Articulo(models.Model):
    # Blogs a los que pertenece el articulo
    blog = models.ManyToManyField(Blog)
    titulo = models.CharField(max_length=128, default="", blank=False)
    # Fragmento de URL que seguira a la url del blog e identifica este articulo
    url = models.SlugField(max_length=512, default="", unique=False, blank=True)
    contenido = models.TextField(default="", blank=False)
    publicado = models.BooleanField(default=False)
    bloqueado = models.BooleanField(default=False)
    autores = models.ManyToManyField(User, blank=True)
    colectivos = models.ManyToManyField(Group, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    publicacion = models.DateTimeField(blank=False)
    def save(self, *args, **kwargs):
        # NOTA: mejorar sistemas de URLs amigables
        if self.url == "":
            self.url = slughifi(self.titulo+'-'+unicode(self.creado)[0:10])
        else:
            self.url = slughifi(self.url)
        super(Articulo, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo)
    autor = models.CharField(max_length=64, default="", blank=True)
    email = models.EmailField(default="", blank=True)
    texto = models.TextField(max_length=256, default="", blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    moderado = models.BooleanField(default=False)
    def __unicode__(self):
        return self.texto

