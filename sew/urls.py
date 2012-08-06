from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from sew.views import index


urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^blog/', include('blogs.urls')),
    url(r'^admin/blogs/objetoblog/upload$',
        'blogs.admin_views.importar_objeto_blog',
        name="admin_importar_objecto_blog"),
    url(r'^admin/chronograph/job/(?P<pk>\d+)/run/$',
        'chronograph.views.job_run', name="admin_chronograph_job_run"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
)

# No usar en produccion, servirlos configurando el servidor HTTP
urlpatterns += patterns('', (r'^estaticos/(?P<path>.*)$',
    'django.views.static.serve',
    {
        'document_root': settings.STATIC_ROOT,
        'show_indexes': True,
    }),)
