# -*- encoding: UTF-8 -*-
from xml.dom import minidom


class ConfiguracionXML(object):
    """ Clase para manejar archivos de configuración XML """

    def cadena_configuracion_xml(self, xml):
        """ Prepara un DOM del XML de la cadena para leer la configuracion """
        self._configuracion = minidom.parseString(xml)
        self._configuracion = self._configuracion.childNodes[0]
        self._cache_configuracion = {}

    def valor_configuracion(self, elemento):
        """ Recupera valores configurados en el XML y los cachea """
        if not elemento in self._cache_configuracion:
            nodo = self._configuracion.getElementsByTagName(elemento)[0]
            self._cache_configuracion[elemento] = nodo.childNodes[0].nodeValue
        return self._cache_configuracion[elemento]
