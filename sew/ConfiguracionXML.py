# -*- encoding: UTF-8 -*-
from xml.dom import minidom
import os.path


class ConfiguracionXML(object):
    """ Clase para manejar archivos de configuración XML """

    def __init__(self, xml):
        self._cache_configuracion = {}
        if os.path.isfile(xml):
            pass
        else:
            self._configuracion = minidom.parseString(xml)
            self._configuracion = self._configuracion.childNodes[0]

    def configuracion(self, elemento):
        """ Recupera valores configurados en el XML """
        if not elemento in self._cache_configuracion:
            try:
                nodo = self._configuracion.getElementsByTagName(elemento)[0]
                nodo = nodo.childNodes[0]
                self._cache_configuracion[elemento] = nodo.nodeValue.strip()
            except:
                self._cache_configuracion[elemento] = None
        return self._cache_configuracion[elemento]
