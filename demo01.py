#!/usr/bin/env python3

#Création d'un dictionnaire
mon_dictionnaire = dict()
mon_dictionnaire2 = {}

#Afficher le type pour vérification
print(type(mon_dictionnaire))
print(type(mon_dictionnaire2))

#Remplir le dictionnaire (clé : valeur)
mon_dictionnaire = {"Voiture":"Yaris","Moteur":"4ch","Portes":5}
print(mon_dictionnaire)

#Ajout d'une entrée dans le dictionnaire
mon_dictionnaire["Sièges"] = 5
print(mon_dictionnaire)

#Afficher une valeur de clé
print(mon_dictionnaire["Moteur"])

#Suppression d'une entrée dans le dictionnaire
del mon_dictionnaire["Portes"]
print(mon_dictionnaire)

#Boucle sur les clés d'un dictionnaire
for cle in mon_dictionnaire.keys():
    print(cle)

#Boucle sur les valeurs d'un dictionnaire
for valeurs in mon_dictionnaire.values():
    print(valeurs)

#Boucle sur un dictionnaire (clé et valeurs)
for cle,valeur in mon_dictionnaire.items():
    print(cle, valeur)

#Création d'une liste
ma_liste = list()
ma_liste2 = []

#Affichage du type pour vérification
print(type(ma_liste))
print(type(ma_liste2))

#Remplir la liste
ma_liste = [1,2,3,"Bleu"]
print(ma_liste)

#Ajout d'une entrée dans la liste
ma_liste.append(4)
print(ma_liste)
ma_liste.append("Violet")
print(ma_liste)

#Supprimer une entrée dans la liste
del ma_liste[0]
print(ma_liste)
ma_liste.remove("Bleu")
print(ma_liste)

#Afficher un élément de la liste, ici '3' est un index, ça affichera "Bleu".
print(ma_liste[3])

#Boucle sur une liste
for elements in ma_liste:
    print(elements)

#Boucle avec prise en compte de l'index
for elements in enumerate(ma_liste):
    print(elements)
