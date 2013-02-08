from django.conf.urls import patterns, url

urlpatterns = patterns('admin.views',
    url(r'^$', 'index', name='index'),
    url(r'^aplicaciones-django/$', 'aplicaciones_django',
      name='aplicacionesdjango'),
    url(r'^aplicaciones-django/(.+)/$', 'modelos_django'),
)
