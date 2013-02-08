from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from importlib import import_module
from inspect import isclass
from django.forms import ModelForm
from django.core.context_processors import csrf


def index(request):
    return render_to_response("admin/administracion.htm",
      {
        'STATIC_URL': settings.STATIC_URL,
      })

def aplicaciones_django(request):
    """ Muestra todas las aplicaciones Django instaladas en el proyecto """
    return render_to_response("admin/aplicaciones-django.htm",
    {
        'STATIC_URL': settings.STATIC_URL,
        'APPS_DJANGO': settings.INSTALLED_APPS,
    })

def modelos_django(request, app):
    """ Muestra todos los modelos de una aplicacion Django """
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
    """ Muestra todos los objetos de un modelo """
    modulo = import_module(app + '.models')
    clase_modelo = eval('modulo.' + modelo)
    datos = clase_modelo.objects.all()
    return render_to_response("admin/datos-modelo-django.htm",
    {
        'STATIC_URL': settings.STATIC_URL,
        'DATA_DJANGO': tuple(datos),
    })

def editar_modelo_de_aplicacion_django(request, app, modelo, num_id=None):
    modulo = import_module(app + '.models')
    clase_modelo = eval('modulo.' + modelo)
    class clase_formulario(ModelForm):
        class Meta:
            model = clase_modelo
    if request.POST:
        formulario = clase_formulario(instance=request.POST)
        if formulario.is_valid():
            formulario.save()
        if num_id == None:
            return redirect('datosaplicacionesdjango', app=app, modelo=modelo)
    else:
        if num_id == None:
            formulario = clase_formulario()
        else:
            dato = clase_modelo.objects.get(id=int(num_id))
            formulario = clase_formulario(instance=dato)
    c = {}
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
