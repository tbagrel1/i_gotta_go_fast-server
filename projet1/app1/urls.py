#!/usr/bin/python2
# -*- coding: utf-8 -*

from django.conf.urls import patterns, url

urlpatterns = patterns('app1.views',
    url(r'^accueil$', 'home'),
    url(r'^calc$', 'calc'),
    url(r'^perso$', 'perso'),
    url(r'^getDB$', 'getDB'),
    url(r'^sendScore$', 'sendScore'),
    url(r'^viewScores$', 'viewScores'),
)
