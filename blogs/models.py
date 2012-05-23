from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=32, default="")
    subdirectoriourl = models.CharField(max_length=42, default="")
    descripcion = models.TextField(max_length=256, default="")
    def __unicode__(self):
        return self.titulo

