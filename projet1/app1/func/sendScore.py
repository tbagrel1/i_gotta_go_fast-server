#!/usr/bin/env python3.5
# -*- coding: utf-8 -*

from django.shortcuts import HttpResponse
from app1.models import Score
from Crypto.Cipher import AES

import os
import pickle
import binascii

def _sendScore(request):

    # Définition des fonctions

    def dehex(score):
        try:
            score = binascii.a2b_hex(score.encode("utf-8")).decode("utf-8")
            valid = "OK"
        except:
            score = None
            valid = "Erreur : Hexadecimal Decode"
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
            fichier_checksum = open("app1/func/checksum/checksum.db", "rb")
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
            (valid, score) = dehex(score)
        if valid == "OK":
            (valid, score) = decrypt(score)
        if valid == "OK":
            (valid, score) = depickle(score)
        if valid == "OK":
            (valid, score) = dechecksum(score)
        if valid == "OK":
            valid = addDB(score)

    return HttpResponse(valid)
