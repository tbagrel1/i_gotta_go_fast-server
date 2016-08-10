#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # On génère un rendu basé sur le template base.html
    # situé dans le repertoire templates/app1
    return render(request, 'app1/base.html',
                  {'titre': "Accueil",
                   'body': "Coucou !"})

def viewScores(request):
    from .core.viewScores import _viewScores
    return _viewScores(request)

def sendScore(request):
    from .core.sendScore import _sendScore
    return _sendScore(request)

def getDB(request):
    from .core.getDB import _getDB
    return _getDB(request)

def testConnection(request):
    from .core.testConnection import _testConnection
    return _testConnection(request)
