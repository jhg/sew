from django.db import models

class Blogs(models.Model):
    titulo = models.CharField(max_length=32)

