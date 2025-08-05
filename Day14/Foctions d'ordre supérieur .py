# Exercice : 2

liste_pays = ["France", "Allemagne", "Italie"]
liste_majuscules = [pays.upper() for pays in liste_pays]
print(liste_majuscules) # le resultat est ['France', 'Allemangne','Italie']

numeros = [3, 6, 9, 12, 15]
nouvelle_liste = [i for i, x in enumerate(numeros)]
print(nouvelle_liste)  # [0, 1, 2, 3, 4]

noms = ["jean", "marie", "pierre", "paul"]
noms_majuscules = list(map(str.upper, noms))
print(noms_majuscules)  # ['JEAN', 'MARIE', 'PIERRE', 'PAUL']

pays = ["Islande", "Ireland", "Poland", "Finland", "Thailand", "England", "Switzerland"]

# Filtrer les pays contenant le mot "LAND"
pays_filtres = list(filter(lambda pays: "LAND" in pays.upper(), pays))

print(pays_filtres) # ['Ireland', 'Poland', 'Finland', 'Thailand', 'England']

pays = ["France", "Italie", "Malaisie", "Canada", "Fidji", "Norvege", "Suisse", "Brésil"]

# Filtrer les pays ayant exactement six caractères
pays_filtres = list(filter(lambda pays: len(pays) == 6, pays))

print(pays_filtres)

pays = ["France", "Italie", "Malaisie", "Canada", "Fidji", "Norvege", "Suisse", "Brésil"]

# Filtrer les pays ayant six lettres et plus
pays_filtres = list(filter(lambda pays: len(pays) >= 6, pays))

print(pays_filtres) # le resultat est ['France', 'Italie', 'Malaisie', 'Norvege', 'Suisse']

pays = ["France", "Italie", "Espagne", "Canada", "Egypte", "Norvege", "Suisse", "Brésil", "Estonie"]

# Filtrer les pays commençant par "E"
pays_filtres = list(filter(lambda pays: pays.startswith("E"), pays))

print(pays_filtres) # le résultat est ['Espagne', 'Egypte', 'Estonie']

import itertools

liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']
liste3 = [True, False]

# Chainer les listes
liste_chainée = list(itertools.chain(liste1, liste2, liste3))

print(liste_chainée)  # le résultat est [1, 2, 3, 'a', 'b', 'c', True, False]

from functools import reduce

nombres = [1, 2, 3, 4, 5]

# Utiliser reduce pour additionner les nombres
somme = reduce(lambda x, y: x + y, nombres)

print(somme) # le résultatest 15 

from functools import reduce

pays = ["l'Estonie", "la Finlande", "la Suède", "le Danemark", "la Norvège", "l'Islande"]

# Utiliser reduce pour concaténer les pays
if len(pays) > 1:
    phrase = reduce(lambda x, y: x + ", " + y if not y == pays[-1] else x + " et " + y, pays)
else:
    phrase = pays[0]

phrase += " sont en Europe du Nord"
print(phrase) # Le résultat est l'Estonie, la Finlande, la Suède, le Danemark, la Norvège et l'Islande sont en Europe du Nord
 
def(pays_modeles) 
    
 return pays.filter{(pay => pay.toLowerCase().includes(modele.toLowerCase()));} 


def count_countries_by_first_letter(pays):
    result = {}
    for pay in pays:
        first_letter = pay[0].upper()
        if first_letter in result:
            result[first_letter] += 1
        else:
            result[first_letter] = 1
    return result

   get_first_ten_countries = [ "Afghanistan", "Afrique du Sud", "Albanie", "Algérie", "Allemagne", "Andorre", "Angola", "Antigua-et-Barbuda",
    "Arabie saoudite", "Argentine", "Arménie", "Australie", "Autriche", "Azerbaïdjan", "Bahamas", "Bahreïn"]

def get_first_ten_countries(pays):
    return pays[:10]
print(get_first_ten_countries(pays)) 

def get_last_ten_countries(pays):
    return pays[-10:]

print(get_last_ten_countries(pays))

# Exercice : 1
# map applique une fonction à chaque élément d'une séquence et renvoie une nouvelle séquence avec les résultats.
# filter sélectionne les éléments d'une séquence qui satisfont à une condition donnée et renvoie une nouvelle séquence avec ces éléments.
# reduce applique une fonction de manière cumulative à une séquence et renvoie un résultat unique.

 # Les fonctions d'ordre supérieur sont des fonctions qui prennent des fonctions en argument et/ou renvoient des fonctions en résultat.
# Les fermetures sont des fonctions qui ont accès à leur propre scope et au scope de la fonction qui les a créées, et peuvent maintenir un état interne.
# Les décorateurs sont des fonctions qui prennent des fonctions en argument et renvoient de nouvelles fonctions qui "emballent" les fonctions originales, permettant d'ajouter des fonctionnalités sans modifier le code original.

- Fonction qui double un nombre :
```
```
def double(x):
return x * 2

*   Fonction qui met un string en majuscule :
    python
def majuscule(s):
    return s.upper()

- Fonction qui calcule le carré d'un nombre :


def carre(x):
return x ** 2


### Fonctions d'appel pour filter
#  Fonction qui vérifie si un nombre est pair :
    python
def est_pair(x):
    return x % 2 == 0

# Fonction qui vérifie si un string est vide :

def est_vide(s):
return len(s) == 0
 Fonction qui vérifie si un nombre est positif :
    python
def est_positif(x):
    return x > 0


# Fonctions d'appel pour reduce*
# Fonction qui additionne deux nombres :


def addition(a, b):
return a + b

#   Fonction qui multiplie deux nombres :
    python
def multiplication(a, b):
    return a * b

#  Fonction qui concatène deux strings :

def concatenation(a, b):
return a + b

pays = [
    "Afghanistan", "Afrique du Sud", "Albanie", "Algérie", "Allemagne", "Andorre", "Angola", "Antigua-et-Barbuda",
    "Arabie saoudite", "Argentine", "Arménie", "Australie", "Autriche", "Azerbaïdjan", "Bahamas", "Bahreïn",
    "Bangladesh", "Barbade", "Belgique", "Belize", "Bénin", "Bhoutan", "Biélorussie", "Birmanie", "Bolivie",
    "Bosnie-Herzégovine", "Botswana", "Brésil", "Brunei", "Bulgarie", "Burkina Faso"]
    for pays_individuel in pays:
    print(pays_individuel)

    nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for nombre in nombres:
    print(nombre)
