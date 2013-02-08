from django.conf.urls import patterns, url

urlpatterns = patterns('admin.views',
    url(r'^$', 'index', name='index'),
    url(r'^aplicaciones-django/$', 'aplicaciones_django',
      name='aplicacionesdjango'),
    url(r'^aplicaciones-django/([a-zA-Z0-9.]+)/$', 'modelos_django'),
    url(r'^aplicaciones-django/([a-zA-Z0-9.]+)/([a-zA-Z0-9.]+)/$', 'modelo_de_aplicacion_django'),
)
