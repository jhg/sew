from django.conf.urls import patterns, url

urlpatterns = patterns('admin.views',

  url(r'^$', 'index', name='index'),

  url(r'^aplicaciones-dj/$', 'aplicaciones_django',
    name='aplicacionesdjango'),

  url(r'^aplicaciones-dj/([a-zA-Z0-9.]+)/$', 'modelos_django'),

  url(r'^aplicaciones-dj/(?P<app>[a-zA-Z0-9.]+)/(?P<modelo>[a-zA-Z0-9.]+)/$',
    'modelo_de_aplicacion_django', name="datosaplicacionesdjango"),

  url(r'^aplicaciones-dj/([a-zA-Z0-9.]+)/([a-zA-Z0-9.]+)/n/$',
    'editar_modelo_de_aplicacion_django'),

  url(r'^aplicaciones-dj/([a-zA-Z0-9.]+)/([a-zA-Z0-9.]+)/e/([0-9]+)/$',
    'editar_modelo_de_aplicacion_django'),

  url(r'^aplicaciones-dj/([a-zA-Z0-9.]+)/([a-zA-Z0-9.]+)/b/([0-9]+)/$',
    'borrar_modelo_de_aplicacion_django'),

)
