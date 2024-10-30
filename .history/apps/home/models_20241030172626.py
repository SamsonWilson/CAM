# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#c'est une table pour les prestataire.
class Prestataire(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.nom
# c'est une table pour les fond de financement.
