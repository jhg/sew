# -*- encoding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
import tempfile
from zipfile import ZipFile
from sew.ConfiguracionXML import ConfiguracionXML
from blogs.models import ObjetoBlog

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


@staff_member_required
def importar_objeto_blog(request):
    nuevo_objeto_blog_nombre = ''
    nuevo_objeto_blog_actualizado = None
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            temp = tempfile.TemporaryFile()
            for chunk in request.FILES['file'].chunks():
                temp.write(chunk)
            temp.seek(0)
            paquete_zip = ZipFile(temp)
            configuracion = ConfiguracionXML(
                paquete_zip.read('configuracion.xml'))
            if configuracion.configuracion('nombre') != '' \
                and configuracion.configuracion('nombre') != None:
                try:
                    # Comprobamos si existe
                    objeto_actual = ObjetoBlog.objects.get(
                        nombre=configuracion.configuracion('nombre'))
                    # Lo actualizamos
                    objeto_actual.titulo = configuracion.configuracion('titulo')
                    objeto_actual.codigo_servidor = paquete_zip.read('codigo.py')
                    objeto_actual.codigo = paquete_zip.read('codigo.htm')
                    objeto_actual.save()
                    nuevo_objeto_blog_actualizado = True
                except:
                    # Instalamos el nuevo objeto
                    objeto_nuevo = ObjetoBlog(
                        titulo=configuracion.configuracion('titulo'),
                        nombre=configuracion.configuracion('nombre'),
                        codigo_servidor=paquete_zip.read('codigo.py'),
                        codigo=paquete_zip.read('codigo.htm'))
                    objeto_nuevo.save()
                    nuevo_objeto_blog_actualizado = False
                nuevo_objeto_blog_nombre = configuracion.configuracion('nombre')
            paquete_zip.close()
            temp.close()
    form = UploadFileForm()
    return render_to_response(
        'admin/blogs/importar_objecto_blog.htm',
        {'form': form,
        'nombre_objeto_blog': nuevo_objeto_blog_nombre,
        'nuevo_objeto_blog_actualizado': nuevo_objeto_blog_actualizado,
        'host': request.get_host().strip("/")},
        RequestContext(request, {}))
