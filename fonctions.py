# -*-coding:Utf-8 -*
# 1) Créer une fonction qui creer_tableau2d(nb_lignes, nb_colonnes) et renvoi un tableau 2D (liste 2D)
# definition des fonctions
def creer_tableau2d(nb_lignes,nb_colonnes):
    return [[0]*nb_colonnes for _ in range(nb_lignes)] #on pourrait mettre le bloc d'abord
# on part de 0 * le nb colonnes et on va dupliquer la première colonne sur le nb de lignes

def initialise_tableau2d(size_x, size_y, tableau):
    for x in range (size_x):
        for y in range (size_y):
            tableau[x][y] = "*"
# a chaque boucle for, on change toute les colonnes d'une ligne

def affiche_tableau2d(size_x, size_y, tableau):
    for x in range (size_x):
        for y in range(size_y):
            print(tableau[x][y], end ='') #end ='' pour éviter les retour à la ligne après chaque print
        print ("\r") #je fais un retour chariot à chaque fin de boucle for



#utilisation des fonctions
nb_colonnes = 5
nb_lignes = 5

tableau = creer_tableau2d(nb_lignes, nb_colonnes)
print(tableau)

initialise_tableau2d(nb_lignes, nb_colonnes, tableau)
print(tableau)

affiche_tableau2d(nb_lignes, nb_colonnes, tableau)
print(tableau)




# 2) Créer une fonction initialise_tableau2d(nb_lignes, nb_colonnes, tableau) qui initialise le contenu à '*' pour chacun des éléments


# 3) Créer une fonction affiche_tableau2d(nb_lignes, nb_colonnes, tableau) qui affiche le tableau à l'écran