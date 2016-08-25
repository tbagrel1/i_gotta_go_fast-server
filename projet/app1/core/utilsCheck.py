#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

# Import des modules

import pickle
import hashlib

def parserCheck(nom_fichier_check):
    fichier_check = open(nom_fichier_check + ".csv", "r")
    liste_check = fichier_check.readlines()
    fichier_check.close()

    liste_check = [check[:-1] for check in liste_check if check[:-1].strip()]
    liste_check = [check.split(",")[1].strip() for check in liste_check if 
                   check[0] != "~"]

    print(liste_check)

    fichier_check_comp = open(nom_fichier_check + ".db", "w")
    pickle.dump(liste_check, fichier_check_comp)
    fichier_check_comp.close()

def getCheck(nom_fichier_check):
    fichier_check_comp = open(nom_fichier_check + ".db", "r")
    liste_check = pickle.load(fichier_check_comp)
    fichier_check_comp.close()

    return liste_check

def calculerCheck(nom_fichier):
    return hashlib.md5(open(nom_fichier, "rb").read()).hexdigest()

def main():

    def menu():
        choix = raw_input("\nQue voulez-vous faire ?\n    1. Compiler les " + 
                          "checksums\n    2. Obtenir une checksum\n>>> ")
        return choix

    while True:
        choix = menu()
        if choix[0:2] == "1 ":
            parserCheck(choix[2:])
        elif choix[0:2] == "2 ":
            print(calculerCheck(choix[2:]))
        elif choix == "\exit":
            return
        else:
            print("--> Choix incorrect. Recommencez")

    nom_fichier_check = raw_input("Entrez le radical du fichier .csv " +
                                  "contenant les checksums\n>>> ")
    parserCheck(nom_fichier_check)
    print("Compilation effectuée !\n-----")
    print(getCheck(nom_fichier_check))

if __name__ == "__main__":
    main()
