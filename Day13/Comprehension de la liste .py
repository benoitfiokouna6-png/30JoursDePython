Nombres = [-3, -4, -2, -1, 0, 2, 4, 6]

# Filtre uniquement négatif et zéro dans la liste a l'aide de la compréhension de la liste 

nombres_negatifs_et_zero = [n for n Nombres if n <= 0]

print(nombres_negatifs_et_zero) # le resultat est [-4, -3, -2, -1, 0 ]

list_of_lists = [[[1, 2, 3,]], [[4, 5, 6]],[[7, 8, 9]]]

Sortie [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Applatir la liste suivante des listes de liste a une liste unidimensionnelle

liste_aplati = [element for sous_liste in liste_de_listes for element in sous_liste]

print(liste_aplatie) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

[( 0, 1, 0, 0, 0, 0, ),(1, 1, 1, 1, 1, 1, 1),(2, 1, 2, 4, 8, 16, 32), (3, 1, 3 9, 27, 81, 243), (4, 1, 4, 16, 64, 256, 1024),
(5, 5, 25, 125, 625, 3125),(6, 3, 5, 255, 625, 3125),(216, 1296, 7776),(7, 1, 7, 49, 343, 2401, 16807),(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),(10, 1, 10, 100, 1000, 10000, 10000)]

# La liste des tuples 

list_of_tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5, i**) for i in range (11)]

print(list_of_tuples)

Pays = [('Finlande','Helsinki')], [('Suede', <<Stockholm>>)], [(<<Norvege>>,<<Oslo>>)]

# Aplatir la liste suivante a une nouvelle liste 

liste_aplatie = [[nom_pays, nom_pays[:3],: capitale] for sous_liste in pays for nom_pays, capitale in sous_liste]

[['Finlande', 'Fin', 'Helsinki'],
['Suede'],'Sue' 'Stockholm'],
['Norvege','Nor', 'Oslo']

Pays = [[('Finlande','Helsinki')],[('Suede',<<Stockholm>>)],[(<<Norvege>>,<<Oslo>>)]]

liste_dictionnaire = [[{'country': nom_pays,'city': capitale}for
sous_liste in pays for nom_pays,capitale in sous_liste]]
print(liste_dictionnaires)

Noms = [[('Asabeneh','encoreayeh')],[('David','Smith')],[('Donald','Trump')],[('Bill','Gates')]]

# modifions la liste des listes suivantes en une chaines concaténées

liste_concaténées = [f"{nom}{prenom}" for sous_liste in noms for nom,prenom in sous_liste]
print(liste_concatenée)
# ['Asabeneh encoreayeh', 'David Smith','Donald Trump','Bil Gates']

# écrivons une fonctions lambda qui peut résoudre une pente ou une interception Y des fonctions linéaires

m = (y2-y1)/ (x2-x1)

calcul_pente = lambda x1, y1, x2, y2: (y2-y1) / (x2-x1)