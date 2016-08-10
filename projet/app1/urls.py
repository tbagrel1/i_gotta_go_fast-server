#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('projet.app1.views',
                       url(r'^accueil$', 'home'),
                       url(r'^viewScores$', 'viewScores'),
                       url(r'^sendScore$', 'sendScore'),
                       url(r'^getDB$', 'getDB'),
                       url(r'^testConnection$', 'testConnection'))
