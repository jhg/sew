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
        self.site_id = int(settings.SITE_ID)
        del settings

    def render(self, context):
        mensage_error = 'Error en objecto de blog ' + self.nombre
        try:
            # Creamos un diccionario blog para el objeto
            from django.contrib.sites.models import Site
            try:
                blog_actual = Site.objects.get(id=self.site_id).blog_set.get()
                blog = {'id': blog_actual.id,
                        'titulo': blog_actual.titulo,
                        'sitios': None,
                        'publicado': blog_actual.publicado,
                        'bloqueado': blog_actual.bloqueado,
                        'descripcion': blog_actual.descripcion,
                        'creado': blog_actual.creado,
                        'modificado': blog_actual.modificado,
                        'articulos_por_pagina':
                            blog_actual.articulos_por_pagina,
                        'accesos_directos_paginacion':
                            blog_actual.accesos_directos_paginacion,
                        'plantilla': blog_actual.plantilla,
                        'autores': None,
                        'colectivos': None,}
                del blog_actual
            except:
                blog = {'id': -1,
                        'titulo': '',
                        'sitios': None,
                        'publicado': False,
                        'bloqueado': False,
                        'descripción': '',
                        'creado': None,
                        'modificado': None,
                        'articulos_por_pagina': 0,
                        'accesos_directos_paginacion': 0,
                        'plantilla': '',
                        'autores': None,
                        'colectivos': None,}
            del Site
            # Creamos un contexto predeterminado
            contexto_actual = {"nombre_objeto": self.nombre}
            # Sobreescribimos objetos poco seguros
            file = None
            open = None
            Node = None
            if self.codigo_servidor != '':
                # Realizamos unas importaciones seguras para uso del objeto
                import socket
                import time
                from decimal import Decimal
                try:
                    exec self.codigo_servidor
                except:
                    mensage_error = 'Error en codigo Python' \
                        + ' del objecto de blog ' + self.nombre
            from django.template import Context
            return self.plantilla.render(Context(contexto_actual))
        except:
            return '<!-- ' + mensage_error + ' -->'
