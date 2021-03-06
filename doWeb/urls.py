# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from doit.views import hello
from doit.views import DateTimeNow
from doit.views import TimePlus

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'doWeb.views.home', name='home'),
    # url(r'^doWeb/', include('doWeb.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', DateTimeNow),
    url(r'^time/plus/(\d{1,2})/$', TimePlus),
)