#-*- coding: UTF-8 -*-
from blogs.models import Blog, Articulo, Comentario, ObjetoBlog
from django.contrib import admin

admin.site.register(Blog)
admin.site.register(Articulo)
admin.site.register(Comentario)
admin.site.register(ObjetoBlog)
