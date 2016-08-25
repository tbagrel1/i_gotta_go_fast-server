#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

# Import des modules

import pickle

def parserRang(nom_fichier_rang):
    fichier_rang = open(nom_fichier_rang + ".csv", "r")
    liste_rang = fichier_rang.readlines()
    fichier_rang.close()

    liste_rang = [rang[:-1] for rang in liste_rang if rang[:-1].strip()]
    liste_rang = [[elt.strip() for elt in rang.split(",") if elt.strip()] for 
                  rang in liste_rang if rang[0] != "~"]
    liste_dico_rang = []
    for elt in liste_rang:
        dico_rang = {"pseudo": elt[0],
                     "score": elt[1],
                     "cpm": elt[2],
                     "mpm": elt[3],
                     "temps": elt[4],
                     "date": elt[5],
                     "heure": elt[6],
                     "texte_mode_enh": elt[7]}
        liste_dico_rang.append(dico_rang)

    print(liste_dico_rang)

    fichier_rang_comp = open(nom_fichier_rang + ".db", "w")
    pickle.dump(liste_dico_rang, fichier_rang_comp)
    fichier_rang_comp.close()

def getRang(nom_fichier_rang):
    fichier_rang_comp = open(nom_fichier_rang + ".db", "r")
    liste_rang = pickle.load(fichier_rang_comp)
    fichier_rang_comp.close()

    return liste_rang

def main():
    nom_fichier_rang = raw_input("Entrez le radical du fichier .csv " +
                                 "contenant les rangs\n>>> ")
    parserRang(nom_fichier_rang)
    print("Compilation effectuée !\n-----")
    print(getRang(nom_fichier_rang))

if __name__ == "__main__":
    main()
