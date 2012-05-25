from django.conf.urls import patterns, include, url

urlpatterns = patterns('blogs.views',
    url(r'^$', 'index', name="blogs-url"),
    url(r'^(?P<urlblog>\w+)/$', 'blog'),
)
