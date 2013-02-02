from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^usuarios/', include('usuarios.urls')),
    url(r'^escritorio/', include('escritorios.urls')),
    url(r'^admin/', include('admin.urls')),
    # Examples:
    # url(r'^$', 'sew.views.home', name='home'),
    # url(r'^sew/', include('sew.foo.urls')),
)
