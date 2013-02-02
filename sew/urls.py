from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^usuarios/', include('usuarios.urls')),
    url(r'^escritorio/', include('escritorios.urls')),
    # Examples:
    # url(r'^$', 'sew.views.home', name='home'),
    # url(r'^sew/', include('sew.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
