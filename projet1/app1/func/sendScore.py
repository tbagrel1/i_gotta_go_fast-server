from django.shortcuts import render
from app1.models import Score
from Crypto.Cipher import AES

import os
import base64
import pickle

def _sendScore(request):

    # Définition des fonctions

    def debase64(score):
        try:
            score = base64.decodestring(score)
            valid = "OK"
        except:
            score = None
            valid = "Erreur : Base64 Decode"
        return (valid, score)

    def decrypt(score):
        try:
            decodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC,
                               "vecteur_init_16o")
            score = decodeur.decrypt(score)
            while score[-1] == "\0":
                score = score[:-1]
            valid = "OK"
        except:
            score = None
            valid = "Erreur : Decrypt AES"
        return (valid, score)

    def depickle(score):
        try:
            doc_pick = open("temp.tmp", "wb")
            doc_pick.write(score)
            doc_pick.close()
            doc_pick = open("temp.tmp", "rb")
            mon_pickler = pickle.Unpickler(doc_pick)
            score = mon_pickler.load()
            doc_pick.close()
            os.remove("temp.tmp")
            valid = "OK"
        except:
            score = None
            valid = "Erreur : Depickler"
        return (valid, score)

    def dechecksum(score):
        try:
            fichier_checksum = open("checksum/checksum.db", "rb")
            mon_pickler = pickle.Unpickler(fichier_checksum)
            liste_checksum = mon_pickler.load()
            fichier_checksum.close()
        except:
            liste_checksum = []
        if score[0] in liste_checksum:
            score = score[1]
            valid = "OK"
        else:
            score = None
            valid = "Erreur : Checksum"
        return (valid, score)

    def addDB(score):
        try:
            Score.objects.create(pseudo=score["pseudo"],
                                 score=score["score"],
                                 cpm=score["cpm"],
                                 mpm=score["mpm"],
                                 temps=score["temps"],
                                 date=score["date"],
                                 heure=score["heure"],
                                 texte_mode_enh=score["texte_mode_enh"])
            valid = "OK"
        except:
            valid = "Erreur : Ajout DB"
        return valid

    # Programme principal

    score = request.GET.get("score", None)
    valid = "OK"
    if score:
        if valid == "OK":
            (valid, score) = debase64(score)
        if valid == "OK":
            (valid, score) = decrypt(score)
        if valid == "OK":
            (valid, score) = depickle(score)
        if valid == "OK":
            (valid, score) = dechecksum(score)
        if valid == "OK":
            valid = addDB(score)

    return render(request,
                  'app1/base.html',
                  {'titre': "Ajout Score",
                   'body': valid})
