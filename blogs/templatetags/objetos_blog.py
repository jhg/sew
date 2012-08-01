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
        codigo_actual = objeto_actual.codigo
        contexto_actual = Context({"nombre_objeto": nombre_actual})
    except:
        msg = '%r tag not find object of blog' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    try:
        if objeto_actual.codigo_servidor != '':
            exec objeto_actual.codigo_servidor
    except:
        msg = '%r tag error in Python code' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    try:
        return ObjetoBlogNodo(nombre_actual, codigo_actual, contexto_actual)
    except:
        msg = '%r tag error compiling HTML code' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)


class ObjetoBlogNodo(template.Node):
    def __init__(self, nombre, codigo, contexto):
        self.nombre = nombre
        self.codigo = codigo
        self.contexto = contexto
        self.plantilla = Template(self.codigo)

    def render(self, context):
        try:
            return plantilla.render(Context(self.contexto))
        except:
            return 'Error in object of blog' + self.nombre
