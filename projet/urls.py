#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from django.conf.urls.defaults import patterns, include, url

urlpatterns = [
    url(r'^app1/', include('projet.app1.urls')),
]
