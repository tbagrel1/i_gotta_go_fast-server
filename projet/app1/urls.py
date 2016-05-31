#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('projet.app1.views',
    url(r'^accueil$', 'home'),
)
