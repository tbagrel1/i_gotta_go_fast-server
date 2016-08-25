#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from django.shortcuts import HttpResponse

import binascii
from projet.app1.core import utilsCheck

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
        liste_check = utilsCheck.getCheck()
        if checksum in liste_check:
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
