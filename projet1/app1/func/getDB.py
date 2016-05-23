#!/usr/bin/python2
# -*- coding: utf-8 -*

from django.shortcuts import HttpResponse
from app1.models import Score

import pickle
import os

def _getDB(request):
    try:
        tab = list(Score.objects.order_by('-score'))
        db = []
        for ligne in tab:
            dico_score = {"pseudo": ligne.pseudo,
                          "score": ligne.score,
                          "cpm": ligne.cpm,
                          "mpm": ligne.mpm,
                          "temps": ligne.temps,
                          "date": ligne.date,
                          "heure": ligne.heure,
                          "texte_mode_enh": ligne.texte_mode_enh}
            db.append(dico_score)
    except:
        db = None

    fichier_temp = open("app1/func/temp_getDB.tmp", "wb")
    mon_pickler = pickle.Pickler(fichier_temp)
    mon_pickler.dump(db)
    fichier_temp.close()
    fichier_temp = open("app1/func/temp_getDB.tmp", "rb")
    retour = fichier_temp.read().encode('hex')
    fichier_temp.close()
    os.remove("app1/func/temp_getDB.tmp")

    return HttpResponse(retour)
