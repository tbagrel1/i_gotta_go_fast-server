#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from django.conf.urls import url, patterns

urlpatterns = patterns('blog.views',
    url(r'^accueil$', 'home')
)
