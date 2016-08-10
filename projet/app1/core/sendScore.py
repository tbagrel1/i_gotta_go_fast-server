#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from django.shortcuts import HttpResponse
from projet.app1.models import Score
from Crypto.Cipher import AES

import os
import pickle
import binascii

def _sendScore(request):

    # Définition des fonctions

    def dehex(score):
        try:
            score = binascii.a2b_hex(score)
            valid = "OK"
        except:
            score = None
            valid = "Erreur : Hexadecimal Decode"
        return (valid, score)

    def decrypt(score):
        try:
            decodeur = AES.new("Wvab2rFaKiCNP5W4", AES.MODE_CBC,
                               "PFaP61MX9pax9MmB")
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
            score = pickle.loads(score)
            valid = "OK"
        except:
            score = None
            valid = "Erreur : Depickler"
        return (valid, score)

    def dechecksum(score):
        fichier = open("core/checksum.db", "r")
        liste_lignes = fichier.readlines()
        fichier.close()
        # On ne récupère que les lignes qui sont non vides et qui ne 
        # commencent pas par un '#'
        liste_lignes = [ligne[:-1].strip() for ligne in liste_lignes if 
                        ligne[:-1].strip() and ligne[:-1].strip()[0] != "#"]
        if score[0] in liste_lignes:
            score = score[1]
            valid = "OK"
        else:
            score = None
            valid = "Erreur : Checksum"
        return (valid, score)

    def addDB(score):
        try:
            Score.objects.create(aff=score["aff"],
                                 pseudo=score["pseudo"],
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
