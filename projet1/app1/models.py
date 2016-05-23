# -*- coding: utf-8 -*
from django.db import models

# Create your models here.

class Score(models.Model):
    pseudo = models.CharField(max_length=21, verbose_name="Pseudo")
    score = models.IntegerField(verbose_name="Score")
    cpm = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Caractères par minute")
    mpm = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Mots par minute")
    temps = models.IntegerField(verbose_name="Temps choisi")
    date = models.DateField(verbose_name="Date")
    heure = models.TimeField(verbose_name="Heure")
    texte_mode_enh = models.CharField(max_length=50, verbose_name="Texte utilisé")

    def __str__(self):
        """Cette méthode permet de reconnaître facilement l'objet"""
        return (self.pseudo)

