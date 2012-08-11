#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os


def _confirmado(pregunta):
    """ Pide al usuario una confirmación """
    respuesta = raw_input('\n  ¿' + pregunta + '? (S/N): ')
    if respuesta == 'N' or respuesta == 'n':
        return False
    return True

def _menu(titulo='Menu de opciones', *menu):
    """ Muestra al usuario un menu """
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

if __name__ == '__main__':
    print 'Bienvenido al asistente de SEW.'
    _opcion = _menu(
        '¿Como esta ejecutando este asistente?',
        'Es la primera vez',
        'No es la primera vez',
        'No estoy seguro')
    if _opcion == 1:
        _instalar = True
    elif _opcion == 2:
        _instalar = False
    else:
        _instalar = None
    if _confirmado('Puedo eliminar archivos .pyc') and not _instalar:
        print 'Eliminando archivos de bytecode de Python...'
        os.system("find ./ -name \\*.pyc -exec rm {} \\;")
        print 'Eliminados, ahora se generaran al ejecutar un .py otra vez'
