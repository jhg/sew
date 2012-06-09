from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from settings_local import HOST
from blogs.models import Blog

def index(request):
    blogs = Blog.objects.all()
    num_blogs = len(blogs)
    return render_to_response('blogs/index.htm', locals())

def blog(request, urlblog):
    try:
        blog = Blog.objects.get(url=urlblog) # Encontramos el blog por su url
        # Extraemos los articulos publicados en este blog y los ordenamos
        articulos = blog.articulo_set.filter(publicado=True)
        articulos = articulos.order_by("publicacion").reverse()
        # Paginacion de los articulos
        paginacion = Paginator(articulos, blog.articulos_por_pagina)
        pagina = request.GET.get('pagina')
        try:
            articulos = paginacion.page(pagina)
        except PageNotAnInteger:
            articulos = paginacion.page(1)
        except EmptyPage:
            articulos = paginacion.page(paginacion.num_pages)
        return render_to_response('blogs/blog_index.htm', locals())
    except:
        blogs = Blog.objects.all()
        num_blogs = len(blogs)
        host = HOST.strip("/")
        return render_to_response('blogs/blog_inexistente.htm', locals())

