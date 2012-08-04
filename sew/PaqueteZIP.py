# -*- encoding: UTF-8 -*-
from sew.ConfiguracionXML import ConfiguracionXML
from zipfile import ZipFile


class PaqueteZIP(ZipFile, ConfiguracionXML, object):
    """ Clase para manipular paquetes comprimidos con ZIP (paquetes de
        software, multimedia, estilos, etc) """

    def __init__(self, ruta, modo='rb'):
        self._archivo = open(ruta, modo)
        ZipFile.__init__(self, self._archivo)
        ConfiguracionXML.__init__(self, self.read('configuracion.xml'))

    def close(self):
        self.cerrar()

    def cerrar(self):
        """ Cierra el archivo del paquete abierto """
        ZipFile.close(self)
        self._archivo.close()

    def leer(self, archivo, clave=None):
        """ Devuelve todo el contenido de un archivo del paquete """
        ZipFile.read(self, archivo, clave)

    def listado(self):
        """ Devuelve una lista de los nombres de archivo del paquete """
        return ZipFile.namelist(self)
