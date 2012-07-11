from django.conf.urls import patterns, include, url


urlpatterns = patterns('blogs.views',
    url(r'^(?P<urlarticulo>[-\w]+)/$', 'dynamic_articulo_blog'),
    url(r'^$', 'dynamic_blog', name="blogs-url"),
)
