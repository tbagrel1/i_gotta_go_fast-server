#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from django.shortcuts import HttpResponse

import binascii

def _testConnection(request):

    # Définition des fonctions
    def dehex(checksum):
        try:
            checksum = binascii.a2b_hex(checksum)
            valid = "OK"
        except:
            checksum = None
            valid = "Erreur : Hexadecimal Decode"
        return (valid, checksum)

    def dechecksum(checksum):

        fichier = open("projet/app1/core/checksum.db", "r")
        liste_lignes = fichier.readlines()
        fichier.close()
        # On ne récupère que les lignes qui sont non vides et qui ne 
        # commencent pas par un '#'
        liste_lignes = [ligne[:-1].strip() for ligne in liste_lignes if 
                        ligne[:-1].strip() and ligne[:-1].strip()[0] != "#"]

        if checksum in liste_lignes:
            valid = "OK"
        else:
            valid = "Erreur : Checksum"

        return valid

    # Programme principal

    checksum = request.GET.get("checksum", None)
    valid = "OK"
    if valid == "OK":
        (valid, checksum) = dehex(checksum)
    if valid == "OK":
        valid = dechecksum(checksum)

    return HttpResponse(valid)
