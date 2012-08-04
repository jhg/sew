# -*- encoding: UTF-8 -*-
from django.core.management.base import BaseCommand, CommandError
from settings_local import PROJECT_DIR
from blogs.models import ObjetoBlog
import zipfile
from sew.ConfiguracionXML import ConfiguracionXML


class Command(BaseCommand, ConfiguracionXML):
    help = "Importa objetos de blog comprimidos en ZIP"
    args = "[archivo]"

    def handle(self, *args, **options):
        titulo, nombre_nuevo, codigo_servidor, codigo = self._extraer(args[0])
        if nombre_nuevo != '':
            try:
                # Comprobamos si existe
                objeto_actual = ObjetoBlog.objects.get(nombre=nombre_nuevo)
                # Lo actualizamos
                objeto_actual.titulo = titulo
                objeto_actual.codigo_servidor = codigo_servidor
                objeto_actual.codigo = codigo
                objeto_actual.save()
                print 'Objeto actualizado'
            except:
                # Instalamos el nuevo objeto
                objeto_nuevo = ObjetoBlog(
                    titulo=titulo,
                    nombre=nombre_nuevo,
                    codigo_servidor=codigo_servidor,
                    codigo=codigo)
                objeto_nuevo.save()
                print 'Instalado nuevo objeto ' + nombre_nuevo

    def _extraer(self, ruta):
        archivo_zip = open(ruta, 'rb')
        objeto_zip = zipfile.ZipFile(archivo_zip)
        codigo_servidor = ''
        codigo = ''
        titulo = ''
        nombre = ''
        self.cadena_configuracion_xml(objeto_zip.read('configuracion.xml'))
        try:
            codigo_servidor = objeto_zip.read('codigo.py')
        except:
            pass
        try:
            codigo = objeto_zip.read('codigo.htm')
        except:
            pass
        archivo_zip.close()
        titulo = self.valor_configuracion("titulo")
        nombre = self.valor_configuracion("nombre")
        return titulo, nombre, codigo_servidor, codigo
