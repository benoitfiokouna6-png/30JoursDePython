# sets

it_companies = { 'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon' }

A = {19,22,24,20,25,26}

b = {19,22,20,25,26,24,28,27}

Ages =[22,19,24,25,26,24,25,24]

# la longueur de l'ensemble it_companies

print(len(it_companies)) # la longueur de l'ensemble it_companies est 7

# ajouter un élément a l'ensemble it_companies

it_companies.add('twitter')

print(it_companies) # l'ensemble it_companies après ajout de twitter est {'facebook', 'google', 'microsoft', 'apple', 'ibm', 'oracle', 'amazon', 'twitter'}

# insertion de plusieurs éléments a la fois a l'ensemble it_companies

it_companies.update([ 'html', 'css', 'snapchat', 'whatsapp'])

print(it_companies)

# supprimer une des des sociétés de l'ensemble it_companies

it_companies.remove('Apple')

print(it_companies) # l'ensemble it_companies après suppression de apple est { 'Facebook', 'Google', 'Microsoft',  'IBM', 'Oracle', 'Amazon', 'html', 'css', 'snapchat', 'whatsapp' }

# la différence entre supprimer et rejéter

it_companies.discard('whatsapp') # supprime watsapp dans l'ensemble it_companies

it_companies.remove('css') # rejeter css dans l'ensemble it_companies 

Exercie:2

# rejoignez A et B

C = A.union(b)
print(C) # l'ensemble C est {19,20,22,24,25,26,27,28}

# une insertion B

C.update(b)

print(C) # l'ensemble C est {19,20,22,24,25,26,27,28}

# sous-ensemble

print(B.issubset(C)) # True, B est un sous-ensemble de C

# les ensembles disjoints

print(A.isdisjoint(b)) # False, A et B ont des éléments en commun

# rejoindre A et B

D = A.intersection(b)

print(D) # l'ensemble D est {19,20,22,24,25,26}

# la différence symétrique entre A et B

E = A.symmetric_difference(b)

print(E) # l'ensemble E est {28, 19, 20, 22, 24, 25, 26, 27}

# supprimer tous les éléments de l'ensemble it_companies

it_companies.clear() # l'ensemble it_companies est vide

Exercice:3

# convertir la liste Ages en ensemble

ages_set = set(Ages)

# la longueur de l'ensemble ages_set
print(len(ages_set)) # la longueur de l'ensemble ages_set est 6

# la difference entre les types de données suivants: chaine, liste, tuple, ensemble
# Chaine: séquence de caractères immuable, utilisée pour représenter du texte.
# Liste: collection ordonnée et modifiable d'éléments, pouvant contenir des doublons.
# Tuple: collection ordonnée et immuable d'éléments, pouvant contenir des doublons.
# Ensemble: collection non ordonnée d'éléments uniques, sans doublons.

Phrase = 'I am a teacher and i love to inspire and teach people.'

# nombre de mots uniques utilisés dans la phrase
unique_words = set(Phrase.split())
print(len(unique_words)) # le nombre de mots uniques dans la phrase est 13


