# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# admin.py

from django.contrib import admin
from .models import Prestataire,Fond_Financement

# Enregistrement simple du modèle Produit
admin.site.register(Prestataire)
admin.site.register(Fond_Financement)

