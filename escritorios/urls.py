from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('escritorios.views',
    url(r'^$', 'escritorio', name='escritorio'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^estaticos/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    )
