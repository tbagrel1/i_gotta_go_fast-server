#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from django.shortcuts import HttpResponse
from projet.app1.models import Score

import pickle
import os
import binascii

def _getDB(request):
    try:
        tab = list(Score.objects.order_by('-score'))
        db = []
        for ligne in tab:
            dico = {"pseudo": ligne.pseudo.encode("utf-8"),
                    "score": int(ligne.score),
                    "cpm": float(ligne.cpm),
                    "mpm": float(ligne.mpm),
                    "temps": int(ligne.temps),
                    "date": unicode(ligne.date).encode("utf-8"),
                    "heure": unicode(ligne.heure).encode("utf-8"),
                    "texte_mode_enh": ligne.texte_mode_enh.encode("utf-8")}
            db.append(dico)
    except:
        db = None

    fichier_temp = open(os.getcwd() +
                        "/projet/app1/func/temp_getDB.tmp", "wb")
    mon_pickler = pickle.Pickler(fichier_temp)
    mon_pickler.dump(db)
    fichier_temp.close()
    fichier_temp = open(os.getcwd() +
                        "/projet/app1/func/temp_getDB.tmp", "rb")
    retour = binascii.b2a_hex(fichier_temp.read())
    fichier_temp.close()
    os.remove(os.getcwd() + "/projet/app1/func/temp_getDB.tmp")

    return HttpResponse(retour)
