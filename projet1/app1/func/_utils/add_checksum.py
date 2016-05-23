#!/usr/bin/python2
# -*- coding: utf-8 -*

import hashlib
import pickle

try:
    fichier_checksum = open("app1/func/checksum/checksum.db", "rb")
    mon_pickler = pickle.Unpickler(fichier_checksum)
    liste_checksum = mon_pickler.load()
    fichier_checksum.close()
except:
    liste_checksum = []

nom = raw_input("Chemin du fichier :\n>>> ")
checksum = hashlib.md5(open(nom, "rb").read()).hexdigest()

liste_checksum.append(checksum)
print(liste_checksum)

fichier_checksum = open("app1/func/checksum/checksum.db", "wb")
mon_pickler = pickle.Pickler(fichier_checksum)
mon_pickler.dump(liste_checksum)
fichier_checksum.close()
