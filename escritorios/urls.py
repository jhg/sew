from django.conf.urls import patterns, url

urlpatterns = patterns('escritorios.views',
    url(r'^$', 'escritorio', name='escritorio'),
)
