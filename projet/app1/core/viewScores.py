#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from django.shortcuts import HttpResponse
from projet.app1.models import Score

import binascii
from projet.app1.core import utilsRang

def _viewScores(request):

    # Définition des fonctions
    def dehex(valeur):
        try:
            valeur = binascii.a2b_hex(valeur)
        except:
            valeur = None
        return valeur

    # Corps du programme

    pseudo_cur = request.GET.get("pseudo", "")
    date_cur = request.GET.get("date", "")
    heure_cur = request.GET.get("heure", "")

    pseudo_cur = dehex(pseudo_cur)
    date_cur = dehex(date_cur)
    heure_cur = dehex(heure_cur)

    try:
        db = list(Score.objects.order_by('-score'))
        db = [{"pseudo": unicode(elt.pseudo).encode("utf-8"),
               "score": str(elt.score),
               "cpm": str(float(elt.cpm)),
               "mpm": str(float(elt.mpm)),
               "temps": str(elt.temps),
               "date": unicode(elt.date).encode("utf-8"),
               "heure": unicode(elt.heure).encode("utf-8"),
               "texte_mode_enh": unicode(elt.texte_mode_enh).encode("utf-8")}
              for elt in db if bool(elt.aff) is True]
    except:
        db = None
    if db:
        liste_rang = utilsRang.getRang("projet/app1/core/rang")
        for i in range(len(liste_rang)):
            liste_rang[i]["pseudo"] = "#" + liste_rang[i]["pseudo"]
        db += liste_rang
        db = sorted(db, key=lambda elt: int(elt["score"]), reverse=True)
        # Ici on ajoute les autres scores 

        c = """<html lang="fr">
    <head>
        <meta charset="UTF-8" />
        <style>
            *
            {
                font-family: "Comic sans MS", Verdana, sans-serif;
                font-size: 13px;
            }

            #normal
            {

            }

            #best
            {
                background-color: yellow;
            }

            #self
            {
                background-color: red;
            }

            #cat
            {
                background-color: gray;
            }
        </style>

        <title>Scores IGGF</title>
    </head>

    <body>
        <table>
            <tr>
                <td>Pseudo</td>
                <td>Score</td>
                <td>Caractères par minute</td>
                <td>Mots par minute</td>
                <td>Temps de jeu</td>
                <td>Date</td>
                <td>Heure</td>
                <td>Texte choisi</td>
            </tr>
"""

        pas_encore_trouve_best = True

        for elt in db:
            type_ligne = ""
            if str(elt["pseudo"])[0] == "#":
                type_ligne = "cat"
            elif pas_encore_trouve_best:
                type_ligne = "best"
                pas_encore_trouve_best = False
            elif (str(elt["pseudo"]) == pseudo_cur and
                  str(elt["date"]) == date_cur and
                  str(elt["heure"]) == heure_cur):
                type_ligne = "self"
            else:
                type_ligne = "normal"

            c += """            <tr id={}>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
    """\
                .format(type_ligne,
                        elt["pseudo"],
                        elt["score"],
                        elt["cpm"],
                        elt["mpm"],
                        elt["temps"],
                        elt["date"],
                        elt["heure"],
                        elt["texte_mode_enh"])
        c += """        </table>
    </body>
</html>"""

    else:
        c = "Erreur : Aucun score"

    return HttpResponse(c)
