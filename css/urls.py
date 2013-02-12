from django.conf.urls import patterns, url

urlpatterns = patterns('css.views',
    url(r'^(?P<fcss>[a-zA-Z0-9.]+).css$', 'css', name="cssdinamico"),
)
