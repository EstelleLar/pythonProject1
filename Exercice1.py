# -*-coding:Utf-8 -*
# 1 écrire un algo qui demande un entier à l'utilisateur, teste si ce nombre est positif ou non et affiche positif et négatif
# i_entier = int(input ("veuillez saisir un nombre entier:"))
# print(i_entier)
# # 1.2 tester si le nombre est positif
# if i_entier >=0:
#     #afficher positif
#     print("la valeur saisie est positif")
# else:
#     #afficher négatif
#     print("la valeur saisie est négative")
# good
#2Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictement
#négatif, et affiche ce résultat.
#on demande un entier

# i_entier= int(float((input ("veuillez saisir un nombre entier:")))
# print(i_entier)
# #teste si  positif
# if i_entier>=0:
#     print("la valeur est positive")
# #teste si nul
# elif i_entier==0:
#     print("la valeur est nulle")
# #teste si négatif
# else:
#     print ("la valeur est négative")
#good attention à la syntaxe

#3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction
#prédéfinie évidemment).
#demander un réel
# a=float(input("veuillez rentrer un nombre réel"))
# a=abs(a)
# ou pour afficher la valeur absolue if i_reel<0: i_reel=-i_reel
# print(a)
#attention si on a fait la deuxieme, il faudra faire afficher str +i_reel
#good


#4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis
#à l’entier supérieur).
# i_reel = float(input("veuillez rentrer un nombre réel"))
# # arrondir à la valeur plus proche, on va tronquer
# i_tronque=int(i_reel)
# delta = i_reel - i_tronque
#
# i_arrondi = i_tronque
# if delta >= 0.5 and i_reel >= 0:
#     i_arrondi = i_tronque + 1
# elif delta <= -0.5 and i_reel < 0: #pour les reels negatifs
#     i_arrondi = i_tronque - 1
# print ("l'arrondi de",i_reel,"est", i_arrondi)



#5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir
#compte des années bissextiles).

# i_mois = int(input("veuillez entrer le numéro d'un mois: "))
#
# if i_mois == [1,3,5,7,8,10,12]:
# autre moyen: if i_mois ==1 or i_mois == 3 or i_mois==5 etc...
#     print("ce mois contient 31 jours")
# elif i_mois == 2:
#     print("ce mois contient 28 ou 29 jours")
# else:
#     print("ce mois contient 30 jours")

#6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les
#4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans
#(2000 était une année bissextile).
# quand on doit détecter un scyle, on utilise modulo pour savoir si on est sur un site, si c'est diff de 0 pas cycle bissextile, 2000 sera egale a 0. on fait modulo 4
# i_annee = int(input("veuillez écrire une année"))
# if (i_annee%4 == 0 and i_annee%100 !=0) or i_annee%400 ==0:
#     print("année bissextile")
# else:
#     print ("l'année n'est pas bissextile")
# correction
#exemple %4 sur un nombre incrémenté à partir de 0, i%4 va donner 0 1 2 3 0 1 2 3
# i=0
# while i < 10:
#     print(1, "% 4 vaut", i%4)
#     i = i + 1
#si année%4==0 et année%100 != (different)0 et année%400 =à alors bissextile
#7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois)
#et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.

jour = int(input("veuillez saisir le jour "))
mois = int(input("veuillez saisir le mois"))
#hiver 21/12 20/03
if (jour >= 21 and mois == 12) or mois == 1 or mois == 2 or (jour<21 and mois == 3):
    print ("c'est l'hiver")
elif (jour >= 21 and mois == 3) or mois == 4 or mois == 5 or (jour<21 and mois == 6):
    print ("vive le printemps")
elif (jour >= 21 and mois == 6) or mois == 7 or mois == 8 or (jour<21 and mois == 9):
    print ("enfin l'été")
else:
    print ("déjà l'automne")
# ou date = input ("date jj/mm")
# jour = int(date.split ("/")[0]
# mois = int(date.split ("/") [1] on fait un tableau