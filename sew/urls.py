from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from sew.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sew.views.home', name='home'),
    # url(r'^sew/', include('sew.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blogs.urls')),
    url(r'^$', index),
)

# No usar en produccion, servirlos configurando el servidor HTTP
urlpatterns += patterns('', (r'^estaticos/(?P<path>.*)$',
    'django.views.static.serve',
    {
        'document_root': settings.STATIC_ROOT,
        'show_indexes': True,
    }),)

