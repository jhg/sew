from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=512)

