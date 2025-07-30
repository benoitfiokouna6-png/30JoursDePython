# Dictionnaires

# Dictionnaire vide

chien_dct = {}

# ajouter des éléments au dictionnaire chien_dct

chien_dct['nom': 'peach', 'la couleur': 'brun', 'la race': 'golden retriever', 'les jambes': '4', 'age': 3]

# Dictionnaire étudiant

etudiant_dct = {'nom': 'Alice', 'prénom': 'FIOKOUNA', 'sexe': 'F', 'ages': 24,'etat_matrimonial': 'Célibataire','compétences': ['Python', 'Mathématiques', 'Physique'],'pays': 'TOGO', 'ville': 'Lomé', 'adresse': '123 Rue de l\'Université'}

# la longueur du dictionnaire étudiant_dct

print(len(etudiant_dct)) # Affiche la longueur du dictionnaire étudiant_dct

#  obtenir les valeurs du dictionnaire étudiant_dct comme une liste

valeurs_etudiant = list(etudiant_dct.values())
print(valeurs_etudiant) # Affiche les valeurs du dictionnaire étudiant_dct

#  changer le dictionnaire en une liste de tuples
etudiant_tuples = list(etudiant_dct.items())
print(etudiant_tuples) # Affiche la liste de tuples du dictionnaire étudiant_dct

#  supprèssion d'un élément du dictionnaire étudiant_dct
del etudiant_dct['adresse'] # Supprime l'élément 'adresse' du dictionnaire étudiant_dct

# suppression de l'un des dictionnaires

del chien_dct
print(chien_dct) # Affiche le dictionnaire chien_dct après suppression, qui sera vide


