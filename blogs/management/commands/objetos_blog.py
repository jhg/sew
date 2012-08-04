# -*- encoding: UTF-8 -*-
from django.core.management.base import BaseCommand, CommandError
from settings_local import PROJECT_DIR
from blogs.models import ObjetoBlog
from sew.PaqueteZIP import PaqueteZIP


class Command(BaseCommand):
    help = "Importa objetos de blog comprimidos en ZIP"
    args = "[archivo]"

    def handle(self, *args, **options):
        paquete = PaqueteZIP(args[0])
        if paquete.configuracion('nombre') != '' \
            and paquete.configuracion('nombre') != None:
            try:
                # Comprobamos si existe
                objeto_actual = ObjetoBlog.objects.get(
                    nombre=paquete.configuracion('nombre'))
                # Lo actualizamos
                objeto_actual.titulo = paquete.configuracion('titulo')
                objeto_actual.codigo_servidor = codigo_servidor
                objeto_actual.codigo = codigo
                objeto_actual.save()
            except:
                # Instalamos el nuevo objeto
                objeto_nuevo = ObjetoBlog(
                    titulo=paquete.configuracion('titulo'),
                    nombre=paquete.configuracion('nombre'),
                    codigo_servidor=paquete.read('codigo.py'),
                    codigo=paquete.read('codigo.htm'))
                objeto_nuevo.save()
