#-*- coding: UTF-8 -*-

from django.template import Library, Node

register = Library()
del Library


@register.tag
def objeto_blog(parser, token):
    # Realizamos las importaciones solo a nivel de esta funcion por seguridad
    from django.core.cache import cache
    from blogs.models import ObjetoBlog
    from django.template import Template, TemplateSyntaxError
    try:
        nombre_actual = token.split_contents()[1]
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise TemplateSyntaxError(msg)
    try:
        # Intentamos recuperarlo de la cache
        objeto_actual = cache.get('objeto_blog' + nombre_actual)
        if objeto_actual == None:
            # Obtenemos el objeto de blog indicado
            objeto_actual = ObjetoBlog.objects.get(nombre=nombre_actual)
            cache.set('objeto_blog' + nombre_actual, objeto_actual, 900)
            cache.delete('codigo_objeto_blog' + nombre_actual)
    except:
        msg = '%r tag not find object of blog' % token.split_contents()[0]
        raise TemplateSyntaxError(msg)
    try:
        # Intentamos recuperar la plantilla compilada de la cache
        codigo_actual = cache.get('codigo_objeto_blog' + nombre_actual)
        if codigo_actual == None:
            codigo_actual = Template(objeto_actual.codigo)
            cache.set('codigo_objeto_blog' + nombre_actual, codigo_actual, 900)
        codigo_servidor = objeto_actual.codigo_servidor
        return ObjetoBlogNodo(nombre_actual, codigo_actual, codigo_servidor)
    except:
        msg = '%r tag error compiling HTML code' % token.split_contents()[0]
        raise TemplateSyntaxError(msg)


class ObjetoBlogNodo(Node):
    def __init__(self, nombre, plantilla, codigo_servidor):
        from django.conf import settings
        self.nombre = nombre
        self.codigo_servidor = codigo_servidor
        self.plantilla = plantilla
        self.site_id = settings.SITE_ID
        del settings

    def render(self, context):
        try:
            # Realizamos unas importaciones seguras para uso del objeto
            import socket
            import time
            from decimal import Decimal
            # Sobreescribimos objetos poco seguros
            file = None
            open = None
            Node = None
            # Creamos un contexto predeterminado
            contexto_actual = {"nombre_objeto": self.nombre}
            if self.codigo_servidor != '':
                exec self.codigo_servidor
            from django.template import Context
            return self.plantilla.render(Context(contexto_actual))
        except:
            return '<!-- Error en objecto de blog ' + self.nombre + ' -->'
