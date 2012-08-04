# -*- encoding: UTF-8 -*-
from django.core.management.base import BaseCommand, CommandError
from settings_local import PROJECT_DIR
from blogs.models import ObjetoBlog
import zipfile
from sew.ConfiguracionXML import ConfiguracionXML


class Command(BaseCommand):
    help = "Importa objetos de blog comprimidos en ZIP"
    args = "[archivo]"

    def handle(self, *args, **options):
        if nombre_nuevo != '':
            try:
                # Comprobamos si existe
                objeto_actual = ObjetoBlog.objects.get(nombre=nombre_nuevo)
                # Lo actualizamos
                objeto_actual.titulo = titulo
                objeto_actual.codigo_servidor = codigo_servidor
                objeto_actual.codigo = codigo
                objeto_actual.save()
            except:
                # Instalamos el nuevo objeto
                objeto_nuevo = ObjetoBlog(
                    titulo=titulo,
                    nombre=nombre_nuevo,
                    codigo_servidor=codigo_servidor,
                    codigo=codigo)
                objeto_nuevo.save()
