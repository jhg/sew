# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from css.models import HojaCss


def css(request, fcss):
    """ CSS dinamico """
    hoja = HojaCss.objects.get(nombre=fcss)
    reglas = {}
    for selector in hoja.selectorcss_set.all():
        declaraciones = {}
        for declaracion in selector.declaracioncss_set.all():
            declaraciones[declaracion.propiedad] = declaracion.valor
        reglas[selector.valor] = declaraciones
    return render_to_response("css/base.css",
      {
        'reglas': reglas,
      })
