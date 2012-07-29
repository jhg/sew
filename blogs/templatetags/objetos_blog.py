#-*- coding: UTF-8 -*-
from blogs.models import ObjetoBlog
from django import template

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
    return ObjetoBlogNodo(objeto_actual.codigo)


class ObjetoBlogNodo(template.Node):
    def __init__(self, codigo):
        self.codigo = codigo

    def render(self, context):
        return self.codigo
