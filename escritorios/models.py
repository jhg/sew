from django.db import models
from usuarios.models import Usuario

class Escritorio(models.Model):
    propietario = models.ForeignKey(Usuario)
