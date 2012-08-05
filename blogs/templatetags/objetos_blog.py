#-*- coding: UTF-8 -*-
from blogs.models import ObjetoBlog
from django import template
from django.template import Context, Template
from django.core.cache import cache

register = template.Library()


@register.tag
def objeto_blog(parser, token):
    try:
        nombre_actual = token.split_contents()[1]
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
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
        raise template.TemplateSyntaxError(msg)
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
        raise template.TemplateSyntaxError(msg)


class ObjetoBlogNodo(template.Node):
    def __init__(self, nombre, plantilla, codigo_servidor):
        self.nombre = nombre
        self.codigo_servidor = codigo_servidor
        self.plantilla = plantilla

    def render(self, context):
        try:
            # Creamos un contexto predeterminado
            contexto_actual = {"nombre_objeto": self.nombre}
            if self.codigo_servidor != '':
                exec self.codigo_servidor
            return self.plantilla.render(Context(contexto_actual))
        except:
            return '<!-- Error in object of blog ' + self.nombre + ' -->'
