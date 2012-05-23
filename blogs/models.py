from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    titulo = models.CharField(max_length=32, default="")
    suburl = models.CharField(max_length=42, default="")
    autores = models.ManyToManyField(User)
    descripcion = models.TextField(max_length=256, default="")
    def __unicode__(self):
        return self.titulo

