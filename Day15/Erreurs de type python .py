# Imprimer un message

print("Bonjour, monde !")


#  Utiliser des variables

x = 5
y = 3
print(x + y)


#  Utiliser des listes

fruits = ["pomme", "poire", "abricot"]
print(fruits[0])


#  Utiliser des boucles

for i in range(5):
    print(i)


# Utiliser des conditions

x = 5
if x > 10:
    print("x est supérieur à 10")
else:
    print("x est inférieur ou égal à 10")


#  Utiliser des fonctions

def bonjour(nom):
    print(f"Bonjour, {nom} !")

bonjour("Alice")


#  Utiliser des listes avec des boucles

nombres = [1, 2, 3, 4, 5]
for nombre in nombres:
    print(nombre)


#  Utiliser la fonction map

def double(x):
    return x * 2

nombres = [1, 2, 3, 4, 5]
doubles = list(map(double, nombres))
print(doubles)


#  Utiliser la fonction filter

def est_pair(x):
    return x % 2 == 0

nombres = [1, 2, 3, 4, 5]
pairs = list(filter(est_pair, nombres))
print(pairs)


#  Utiliser la fonction reduce

from functools import reduce

def addition(a, b):
    return a + b

nombres = [1, 2, 3, 4, 5]
somme = reduce(addition, nombres)
print(somme)


