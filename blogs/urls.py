from django.conf.urls import patterns, include, url

urlpatterns = patterns('blogs.views',
    url(r'^$', 'index_blog', name="blogs-url"),
    url(r'^(?P<urlblog>[-\w]+)/$', 'blog'),
    url(r'^(?P<urlblog>[-\w]+)/(?P<urlarticulo>[-\w]+)/$', 'articulo_blog'),
)
