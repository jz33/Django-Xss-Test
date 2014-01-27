from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from xss.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',include(admin.site.urls)),
    url(r'^current_datetime/$',current_datetime),
    
    url(r'^index/$', main), # Main
    url(r'^index/xss0/$', xss0), # No Escape
    url(r'^index/xss1/$', xss1), # Escape
    url(r'^index/xss2/$', xss2), # Test

)