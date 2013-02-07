from django.shortcuts import render_to_response
from django.conf import settings

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
