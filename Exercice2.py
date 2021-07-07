# -*-coding:Utf-8 -*
# print ("hello")

# 1. ecrire un algorithme qui demande un entier positif et le rejette tant que le nombre saisi n'est pas conforme
# i = int(input("veuillez saisir un entier positif: "))
# while (i <= 0 or i !=int):
#     i=int(input("veuillez saisir un entier positif "))
#
# else :
#     print ("merci")

# 2. Écrire un algorithme qui demande 10 entiers, compte le nombre d’entiers positifs saisis, et affiche ce résultat.
# on utilise for i in range(10)

#cpt variable compteur cpt =0 pour l'initier à 0

# cpt = 0
# for i in range (10):
#     a = int(float(input("saisir un entier positif ou négatif")))
#     if a >= 0: # pour compter uniquement les entiers positifs
#         cpt = cpt + 1
# print ("le nombre d'entier positif est", cpt)


# 3. Écrire un algorithme qui demande des entiers positifs à l’utilisateur, les additionne, et qui s’arrête en affichant le
# résultat dès qu’un entier négatif est saisi.
# modif exo 1 pour calcul somme

# i = 1
# somme = 0 # variable de comptage
# while i >= 0:
#     i = int(float(input(" saisir un entier positif ")))
#     if i >= 0:
#         somme += i
# # la boucle s'arrête lorsqu'on saisi un nombre négatif
# print("la somme des entiers positifs saisis est égale à", somme)

# 4. Modifier ce dernier algorithme pour afficher la moyenne de la série d’entiers positifs saisis.
# m = 0
# i = 0
# a = 0
# b = 0
# while a >= 0:
#      a = int(float(input(" saisir un entier positif ")))
#      if a >= 0:
#          i = i+1
#          b = b+a
#          m = b/i
# print("la moyenne des entiers positifs saisis est égale à", m)
