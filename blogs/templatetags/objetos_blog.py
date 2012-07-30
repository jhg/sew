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
    return ObjetoBlogNodo(nombre_actual, objeto_actual.codigo)


class ObjetoBlogNodo(template.Node):
    def __init__(self, nombre, codigo):
        self.codigo = codigo

    def render(self, context):
        try:
            plantilla = Template(self.codigo)
            return plantilla.render(Context(locals()))
        except:
            return 'Error in object of blog' + nombre
