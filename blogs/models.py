from django.db import models
from django.contrib.auth.models import User, Group

class Blog(models.Model):
    titulo = models.CharField(max_length=64, default="", blank=False)
    # Fragmento de URL que seguira a la url de blogs e identifica este blog
    url = models.SlugField(max_length=64, default="", unique=True, blank=False)
    publicado = models.BooleanField(default=False)
    bloqueado = models.BooleanField(default=False)
    descripcion = models.TextField(max_length=256, default="", blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    # Autores (individuales) y colectivo de autores (todos los del grupo)
    autores = models.ManyToManyField(User, blank=True)
    colectivos = models.ManyToManyField(Group, blank=True)
    def __unicode__(self):
        return self.titulo

class Articulo(models.Model):
    # Blogs a los que pertenece el articulo
    blog = models.ManyToManyField(Blog)
    titulo = models.CharField(max_length=128, default="", blank=False)
    contenido = models.TextField(default="", blank=False)
    publicado = models.BooleanField(default=False)
    bloqueado = models.BooleanField(default=False)
    autores = models.ManyToManyField(User, blank=True)
    colectivos = models.ManyToManyField(Group, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    publicacion = models.DateTimeField(blank=True)
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

