#!/usr/bin/python2
# -*- coding: utf-8 -*

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app1/base.html',
                  {'titre': "Accueil",
                   'body': "Coucou !"})

def calc(request):
    nombre1 = float(request.GET.get("nombre1", "0"))
    nombre2 = float(request.GET.get("nombre2", "1"))
    resultat = nombre1 + nombre2
    return render(request, 'app1/calc.html',
                  {'nombre1': nombre1,
                   'nombre2': nombre2,
                   'resultat': resultat})

def perso(request):
    titre = request.GET.get("titre", "Perso")
    message = request.GET.get("message", "Tu est très gentil(le) !")
    return render(request, 'app1/base.html',
                  {'titre': titre,
                   'body': message})

def viewScores(request):
    from .func.viewScores import _viewScores
    return _viewScores(request)

def sendScore(request):
    from .func.sendScore import _sendScore
    return _sendScore(request)

def getDB(request):
    from .func.getDB import _getDB
    return _getDB(request)
