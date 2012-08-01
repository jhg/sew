#-*- coding: UTF-8 -*-
from blogs.models import ObjetoBlog
from django import template
from django.template import Context, Template

register = template.Library()

from django import template


@register.tag
def objeto_blog(parser, token):
    try:
        nombre_actual = token.split_contents()[1]
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    try:
        # Obtenemos el objeto de blog indicado
        objeto_actual = ObjetoBlog.objects.get(nombre=nombre_actual)
    except:
        msg = '%r tag not find object of blog' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    try:
        codigo_actual = Template(objeto_actual.codigo)
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
