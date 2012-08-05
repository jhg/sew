# -*- encoding: utf-8 -*-
from django.core.management.base import NoArgsCommand
import os


class Command(NoArgsCommand):
    help = "Asistente de instalación o reparación de SEW interactivo"

    def handle_noargs(self, **options):
        print 'Bienvenido al asistente de SEW.'
        _opcion = self._menu(
            '¿Como esta ejecutando este asistente?',
            'Es la primera vez para realizar la instalación',
            'No es la primera vez, es una reparación',
            'No estoy seguro')
        if _opcion == 1:
            self._instalar = True
        elif _opcion == 2:
            self._instalar = False
        else:
            self._instalar = None
        if self._confirmado('Puedo eliminar archivos .pyc') \
            and not self._instalar:
            print 'Eliminando archivos de bytecode de Python...'
            os.system("find ./ -name \\*.pyc -exec rm {} \\;")
            print 'Eliminados, ahora se generaran al ejecutar un .py otra vez'

    def _confirmado(self, pregunta):
        respuesta = raw_input('\n  ¿' + pregunta + '? (S/N): ')
        if respuesta == 'N' or respuesta == 'n':
            return False
        return True

    def _menu(self, titulo='Menu de opciones', *menu):
        respuesta = False
        while respuesta == False:
            print ' '
            print titulo
            numero = 1
            for opcion in menu:
                print ' ' + str(numero) + ' -  ' + opcion
                numero += 1
            respuesta = raw_input('  Seleccione una opción: ')
            try:
                respuesta = int(respuesta)
                if 0 < respuesta and respuesta <= len(menu):
                    break
                else:
                    print ' No existe esa opción en el menu.'
                    respuesta = False
            except:
                respuesta = False
        return respuesta - 1
