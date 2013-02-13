# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.cache import cache
from css.models import HojaCss


def css(request, fcss):
    """ CSS dinamico """
    reglas = cache.get('css-dinamico-reglas-' + fcss)
    if reglas == None:
        reglas = {}
        hoja = HojaCss.objects.get(nombre=fcss)
        for selector in hoja.selectorcss_set.all():
            declaraciones = {}
            for declaracion in selector.declaracioncss_set.all():
                declaraciones[declaracion.propiedad] = declaracion.valor
            reglas[selector.valor] = declaraciones
        cache.set('css-dinamico-reglas-' + fcss, reglas, 600)
    return render_to_response("css/base.css",
      {
        'reglas': reglas,
      })
