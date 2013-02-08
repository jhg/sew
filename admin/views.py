from django.shortcuts import render_to_response
from django.conf import settings
from importlib import import_module
from inspect import isclass

def index(request):
    return render_to_response("admin/administracion.htm",
      {
        'STATIC_URL': settings.STATIC_URL,
      })

def aplicaciones_django(request):
    return render_to_response("admin/aplicaciones-django.htm",
    {
        'STATIC_URL': settings.STATIC_URL,
        'APPS_DJANGO': settings.INSTALLED_APPS,
    })

def modelos_django(request, app):
    modulo = import_module(app + '.models')
    modelos = []
    for n in dir(modulo):
        if isclass(eval('modulo.' + n)):
            modelos.append(n)
    return render_to_response("admin/modelos-django.htm",
    {
        'STATIC_URL': settings.STATIC_URL,
        'MODELS_DJANGO': tuple(modelos),
    })

def modelo_de_aplicacion_django(request, app, modelo):
    modulo = import_module(app + '.models')
    clase_modelo = eval('modulo.' + modelo)
    datos = clase_modelo.objects.all()
    return render_to_response("admin/datos-modelo-django.htm",
    {
        'STATIC_URL': settings.STATIC_URL,
        'DATA_DJANGO': tuple(datos),
    })
