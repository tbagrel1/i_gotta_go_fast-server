#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from django.shortcuts import HttpResponse
from projet.app1.models import Score

import pickle
import binascii
import os

def _getDB(request):
    try:
        tab = list(Score.objects.order_by('-score'))
        db = []
        for ligne in tab:
            dico = {"aff": bool(ligne.aff),
                    "pseudo": ligne.pseudo.encode("utf-8"),
                    "score": int(ligne.score),
                    "cpm": float(ligne.cpm),
                    "mpm": float(ligne.mpm),
                    "temps": int(ligne.temps),
                    "date": unicode(ligne.date).encode("utf-8"),
                    "heure": unicode(ligne.heure).encode("utf-8"),
                    "texte_mode_enh": ligne.texte_mode_enh.encode("utf-8")}
            if dico["aff"]:
                db.append(dico)
    except:
        db = []

    retour = pickle.dumps(db)
    retour = binascii.b2a_hex(retour)

    #return HttpResponse(retour)
    return HttpResponse(os.getcwd())
