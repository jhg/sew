#-*- coding: UTF-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from paginacionhc.PaginacionMejorada import accesos_directos_rango
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, Template
from django.http import HttpResponse, Http404
from django.conf import settings
from django.contrib.sites.models import Site
from blogs.models import Blog


def blogs(request, plantilla, urlarticulo=""):
    blogs = Blog.objects.filter(publicado=True, bloqueado=False)
    num_blogs = len(blogs)
    host = request.get_host().strip("/")
    blog_url = '/'
    return render_to_response(plantilla, locals())


def index_blog(request):
    return blogs(request, 'blogs/index.htm')
# NOTA: Optimizar y refactorizar todo el código de este archivo
# NOTA: Continuar mejoras


def dynamic_blog(request):
    # Obtenemos el blog de el sitio pedido
    try:
        blog = Site.objects.get(id=int(settings.SITE_ID)).blog_set.get()
    except:
        raise Http404
    if blog.bloqueado:
        return blogs(request, 'blogs/blog_bloqueado.htm')
    if not blog.publicado:
        return blogs(request, 'blogs/blog_inexistente.htm')
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
    blog_url = '/'
    return HttpResponse(plantilla.render(Context(locals())))


def dynamic_articulo_blog(request, urlarticulo):
    # Obtenemos el blog de el sitio pedido
    try:
        blog = Site.objects.get(id=int(settings.SITE_ID)).blog_set.get()
    except:
        raise Http404
    if blog.bloqueado:
        return blogs(request, 'blogs/blog_bloqueado.htm')
    if not blog.publicado:
        return blogs(request, 'blogs/blog_inexistente.htm')
    # Extraemos el articulo
    articulos = blog.articulo_set.filter(publicado=True, url=urlarticulo)
    if articulos.count() == 0:
        return blogs(request, 'blogs/blog_inexistente.htm', urlarticulo)
    # Usamos la propia plantilla del blog
    plantilla = Template('{% extends "blogs/blog_index.htm" %}\n'
        + "{% load i18n static %}\n"
        + blog.plantilla)
    host = request.get_host().strip("/")
    blog_url = '/'
    return HttpResponse(plantilla.render(Context(locals())))
