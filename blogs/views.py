#-*- coding: UTF-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from paginacionhc.PaginacionMejorada import accesos_directos_rango
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.http import HttpResponse
from settings_local import HOST
from blogs.models import Blog

def blogs(plantilla):
    blogs = Blog.objects.filter(publicado=True, bloqueado=False)
    num_blogs = len(blogs)
    host = HOST.strip("/")
    return render_to_response(plantilla, locals())

def index_blog(request):
    return blogs('blogs/index.htm')

# NOTA: Optimizar y refactorizar todo el código de este archivo

def blog(request, urlblog):
    try:
        blog = Blog.objects.get(url=urlblog) #Encontramos el blog por su url
    except:
        return blogs('blogs/blog_inexistente.htm')
    if blog.bloqueado: return blogs('blogs/blog_bloqueado.htm')
    if not blog.publicado: return blogs('blogs/blog_inexistente.htm')
    # Extraemos los articulos publicados en el blog y los ordenamos
    articulos = blog.articulo_set.filter(publicado=True)
    articulos = articulos.order_by("publicacion").reverse()
    # Paginacion de los articulos
    paginacion = Paginator(articulos, blog.articulos_por_pagina)
    try:
        pagina = int(request.GET.get('pagina'))
    except:
        pagina = 1
    anteriores_pag, posteriores_pag = accesos_directos_rango(pagina,
        paginacion.num_pages, blog.accesos_directos_paginacion)
    try:
        articulos = paginacion.page(pagina)
    except PageNotAnInteger:
        articulos = paginacion.page(1)
    except EmptyPage:
        articulos = paginacion.page(paginacion.num_pages)
    # Usamos la propia plantilla del blog
    plantilla = Template('{% extends "blogs/blog_index.htm" %}\n'
        +blog.plantilla)
    return HttpResponse(plantilla.render(Context(locals())))

def articulo_blog(request, urlblog, urlarticulo):
    try:
        blog = Blog.objects.get(url=urlblog) #Encontramos el blog por su url
    except:
        return blogs('blogs/blog_inexistente.htm')
    if blog.bloqueado: return blogs('blogs/blog_bloqueado.htm')
    if not blog.publicado: return blogs('blogs/blog_inexistente.htm')
    # Extraemos el articulo
    try:
        articulos = blog.articulo_set.filter(publicado=True, url=urlarticulo)
    except:
        return blogs('blogs/blog_inexistente.htm')
    # Usamos la propia plantilla del blog
    plantilla = Template('{% extends "blogs/blog_index.htm" %}'
        +'{% block paginacion %}{% endblock %}\n'
        +blog.plantilla)
    return HttpResponse(plantilla.render(Context(locals())))

