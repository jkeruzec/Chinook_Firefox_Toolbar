# -*- coding: utf-8 -*-
#!\bin\python

"""
buildExtension.py
Script de création d'extension Firefox
"""

__author__ = "Julien Keruzec"
__version__ = "1.0"

import glob
import os
import shutil
import zipfile

# Repertoire parent contenant toutes les images à renommer
SRC_DIR = 'C:\Users\jke\Documents\GitHub\Chinook_Firefox_Toolbar\src\*'
BIN_DIR='C:\Users\jke\Documents\GitHub\Chinook_Firefox_Toolbar\bin'
EXTENSION_NAME='xulschoolhello1.xpi'

# Zipper Extension avec fichier

#Intégrer Extension à Firefox




nomFichierTab = []
numeroImage = 0



# Création du tableau pour la règle de nommage des images X-Y.ext avec
# X numéro de colonne
# Y numéro de ligne
# ext extension fichier

for colonne in range(4):
	for ligne in range(8):
		nomFichierTab.append(`ligne` + '-' + `colonne`)
		
# parcours des fichiers du répertoire et renommage
for fichier in glob.glob(ROOT_DIR):
	if os.path.isfile(fichier):
		nomFichier = os.path.basename(fichier)
		cheminFichier = os.path.dirname(fichier)
		ext = nomFichier.split('.')[-1]
		print 'Ancien nom fichier ' + fichier
		print 'Nouveau nom fichier ' + cheminFichier + os.sep + nomFichierTab[numeroImage] + '.' + ext
		os.rename(fichier, cheminFichier + os.sep + nomFichierTab[numeroImage] + '.' + ext)
		numeroImage += 1