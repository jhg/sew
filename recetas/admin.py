#-*- coding: UTF-8 -*-
from recetas.models import Receta, IngredienteReceta, PasoElaboacionReceta
from django.contrib import admin

admin.site.register(Receta)
admin.site.register(IngredienteReceta)
admin.site.register(PasoElaboacionReceta)
