#-*- coding: UTF-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from paginacionhc.PaginacionMejorada import accesos_directos_rango
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.http import HttpResponse
from django.conf import settings
from blogs.models import Blog


def blogs(request, plantilla, urlblog="", urlarticulo=""):
    blogs = Blog.objects.filter(publicado=True, bloqueado=False)
    num_blogs = len(blogs)
    host = request.get_host().strip("/")
    blog_url = urlblog + '/'
    return render_to_response(plantilla, locals())


def index_blog(request):
    return blogs(request, 'blogs/index.htm')
# NOTA: Optimizar y refactorizar todo el código de este archivo
# NOTA: Finalizar el cambio en la forma de implementación y continuar mejoras


def dynamic_blog(request):
    blog_actual = Blog.objects.get(sitio_raiz=int(settings.SITE_ID))
    return blog(request, blog_actual.url, True)


def blog(request, urlblog, dinamico=False):
    try:
        blog = Blog.objects.get(url=urlblog)  # Encontramos el blog por su url
    except:
        return blogs(request, 'blogs/blog_inexistente.htm', urlblog)
    if blog.bloqueado:
        return blogs(request, 'blogs/blog_bloqueado.htm', urlblog)
    if not blog.publicado:
        return blogs(request, 'blogs/blog_inexistente.htm', urlblog)
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
        + blog.plantilla)
    host = request.get_host().strip("/")
    if dinamico:
        blog_url = '/'
    else:
        blog_url = urlblog + '/'
    return HttpResponse(plantilla.render(Context(locals())))


def dynamic_articulo_blog(request, urlarticulo):
    blog_actual = Blog.objects.get(sitio_raiz=int(settings.SITE_ID))
    return articulo_blog(request, blog_actual.url, urlarticulo, True)


def articulo_blog(request, urlblog, urlarticulo, dinamico=False):
    try:
        blog = Blog.objects.get(url=urlblog)  # Encontramos el blog por su url
    except:
        return blogs(request, 'blogs/blog_inexistente.htm', urlblog)
    if blog.bloqueado:
        return blogs(request, 'blogs/blog_bloqueado.htm', urlblog)
    if not blog.publicado:
        return blogs(request, 'blogs/blog_inexistente.htm', urlblog)
    # Extraemos el articulo
    articulos = blog.articulo_set.filter(publicado=True, url=urlarticulo)
    if articulos.count() == 0:
        return blogs(request, 'blogs/blog_inexistente.htm', urlblog,
            urlarticulo)
    # Usamos la propia plantilla del blog
    plantilla = Template('{% extends "blogs/blog_index.htm" %}\n'
        + "{% load i18n static %}\n"
        + blog.plantilla)
    host = request.get_host().strip("/")
    if dinamico:
        blog_url = '/'
    else:
        blog_url = urlblog + '/'
    return HttpResponse(plantilla.render(Context(locals())))
