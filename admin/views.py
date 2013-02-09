# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from importlib import import_module
from inspect import isclass
from django.forms import ModelForm
from django.core.context_processors import csrf


def index(request):
    """ Escritorio web sencillo para la administracion """
    return render_to_response("admin/administracion.htm",
      {
        'STATIC_URL': settings.STATIC_URL,
      })

def aplicaciones_django(request):
    """ Muestra todas las aplicaciones Django instaladas en el proyecto """
    return render_to_response("admin/aplicaciones-django.htm",
    {
        'STATIC_URL': settings.STATIC_URL,
        'items': settings.INSTALLED_APPS,
    })

def modelos_django(request, app):
    """ Muestra todos los modelos de una aplicacion Django """
    modulo = import_module(app + '.models') # Importamos el modulo de modelos
    modelos = []                            # Añadiremos las clases que tengan
    for n in dir(modulo):                   #  un atributo objects para asi
        if isclass(eval('modulo.' + n)):    #  diferenciar modelos de otras
            try:                            #  clases.
                temp = eval('modulo.' + n + '.objects')
                modelos.append(n)
            except:
                pass
    return render_to_response("admin/modelos-django.htm",
    {
        'STATIC_URL': settings.STATIC_URL,
        'items': tuple(modelos),
    })

def modelo_de_aplicacion_django(request, app, modelo):
    """ Muestra todos los objetos de un modelo """
    modulo = import_module(app + '.models') # Importamos el modulo de modelos
    clase_modelo = eval('modulo.' + modelo) # Obtenemos el modelo
    datos = clase_modelo.objects.all()      # Recuperamos todos los objetos
    return render_to_response("admin/datos-modelo-django.htm",
    {
        'STATIC_URL': settings.STATIC_URL,
        'items': tuple(datos),
    })

def editar_modelo_de_aplicacion_django(request, app, modelo, num_id=None):
    """ Edita objetos de modelos o los crea nuevos """
    modulo = import_module(app + '.models') # Importamos el modulo de modelos
    clase_modelo = eval('modulo.' + modelo) # Obtenemos el modelo
    class clase_formulario(ModelForm):      # Clase formulario para el modelo
        class Meta:
            model = clase_modelo
    if request.POST:                                # Si se reciven datos
        formulario = clase_formulario(request.POST) #  creamos el objeto del
        if formulario.is_valid():                   #  formulario y validamos
            formulario.save()                       # Guardamos los datos
        if num_id == None: # Si es un objeto nuevo redireccionamos al listado
            return redirect('datosaplicacionesdjango', app=app, modelo=modelo)
    else:
        if num_id == None: # Nuevo formulario vacio o formulario de edición
            formulario = clase_formulario()
        else:
            dato = clase_modelo.objects.get(id=int(num_id))
            formulario = clase_formulario(instance=dato)
    c = {} # Creamos el contexto por partes para incluir la proteccion CSRF
    c.update(csrf(request))
    c['STATIC_URL'] = settings.STATIC_URL
    c['FORM_DJANGO'] = formulario
    c['MODEL_URL'] = reverse('datosaplicacionesdjango', args=[app, modelo])
    return render_to_response("admin/formulario-modelo-django.htm", c)

def borrar_modelo_de_aplicacion_django(request, app, modelo, num_id):
    """ Borra un objeto de un modelo indicado por su id """
    modulo = import_module(app + '.models')
    clase_modelo = eval('modulo.' + modelo)
    dato = clase_modelo.objects.get(id=int(num_id))
    dato.delete()
    return redirect('datosaplicacionesdjango', app=app, modelo=modelo)
