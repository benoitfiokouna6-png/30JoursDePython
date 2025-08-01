# Boucles

# Itérer de 0 à 10 en utilisant pour la boucle 

for i in range(11):
    print(i)  # Affiche les nombres de 0 à 10

    # Itérer de 10 à 0 en utilisant pour la boucle pendant
for i in range(10, -1, -1):
    print(i)  # Affiche les nombres de 10 à 0

    # écrivons une boucle qui fait sept appels a imprimer () pour imprimer un triangle

for i in range(1, 8):
    print("#" * i)
# Affiche un triangle de 7 lignes avec des #

# écrivons des boucles imbriquées pour imprimer #

for i in range(1, 8):
    for j in range(i):
        print("#", end="")
    print()  # Passe à la ligne suivante après chaque ligne de #

    # imprimons le modèle suivant
# 0*0 = 0 1*1 = 1 2*2 = 4 3*3 = 9 4*4 = 16 5*5 = 25 6*6 = 36 7*7 = 49 8*8 = 64 9*9 = 81 10*10 = 100
for i in range(11):
    print(f"{i}*{i} = {i*i}")

    # itérer dans la liste,['python', 'numpy', 'pandas', 'flask']
    for item in ['python', 'numpy', 'pandas', 'flask']:
        print(item)

        # utilisons pour la boucle pour itérer de 0 à 100 et imprimons les nombres impairs
for i in range(101):
    if i % 2 != 0:
        print(i)  # Affiche les nombres impairs de 0 à 100

# utilisons pour la boucle pour itérer de 0 à 100 et imprimons les nombres 

for i in range(101):
    if i % 2 == 0:
        print(i)
          # Affiche les nombres pairs de 0 à 100

          # Exercice:2

# utilisons pour la boucle pour itérer de 0 à 100 et imprimons la somme des nombres 

somme_de_0_a_100 = 0
for i in range(101):
    somme_de_0_a_100 += i
print(f"La somme de tous les nombres de 0 à 100 est {somme_de_0_a_100}.")

# utilisons pour la boucle pour itérer de 0 à 100 et imprimons la somme de tous les events
somme_des_events = 0
for i in range(101):
    if i % 2 != 0:
        somme_des_events += i
print(f"La somme de tous les nombres impairs de 0 à 100 est {somme_des_events}.")

# utilisons pour la boucle pour itérer de 0 à 100 et imprimons la somme de toutes les chances
somme_des_chaines = 0
for i in range(101):
    if i % 2 == 0:
        somme_des_chaines += i
print(f"La somme de tous les nombres pairs de 0 à 100 est {somme_des_chaines}.")

# Exercices : 3

# inversons l'ordre a l'aide de boucle

liste_de_fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in reversed(liste_de_fruits):
    print(fruit)  # Affiche les fruits dans l'ordre inverse

    # Accédons au dossiers de données et utilisons le ficher Pays .py pour afficher les pays contenant le mot "land"
import os
path = 'Day10/Pays.py'
if os.path.exists(path):
    with open(path, 'r') as file:
        pays = file.readlines()
        for pays in pays:
            if 'land' in pays.lower():
                print(pays.strip())  # Affiche les pays contenant "land"


