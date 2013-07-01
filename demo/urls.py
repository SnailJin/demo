from django.conf.urls.defaults import patterns, include, url
from demo.views import hello

urlpatterns = patterns('',
    url(r'^hello/$', hello),
)