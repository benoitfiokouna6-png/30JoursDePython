# Conditionels

My_age = 30
if My_age >= 30:
    print("Vous êtes assez vieux pour conduire.")

votre_age = 15
if votre_age >= 18:
    print("Vous êtes assez vieux pour conduire.")
else:
    print("Vous avez besoins de 3ans de plus pour apprendre a conduire.")

    # comparaison de My_age et votre_age
if My_age > votre_age:
    print("Vous êtes plus jeune que moi.")
elif My_age < votre_age:
    print("Vous avez 5ans de plus  que moi.")
else:
    print("Nous avons le même âge.")

    # obtenons deux numeros de l'utilisateur a l'invite d'entrée
A = int(input("4: "))
B = int(input("3 4: "))
if A > B:
    print(f"{A} est plus grand que {B}.")

elif A < B:
    print(f"{B} est plus grand que {A}.")

    if A < B and A % 3 == 0:
        print(f"{A} est plus petit que {B} et est un nombre multiple de 3.")

    elif A < B and A % 3 != 0:

 # Exercice:2

# 80- 100, A 70-8

# 9, B 60-69, C 50-59, D 0-49, E

# Pour cet exercice, nous allons écrire un code qui attribue des notes aux élèves en fonction de leur score.
Score = int(input("Entrez votre score (0-100): ")) elif 80 <= Score <= 100:
    print("Votre note est A.")
    
if 80 <= Score <= 100:
    print("Votre note est A.")
elif 70 <= Score < 80:
    print("Votre note est B.")
elif 60 <= Score < 70:
    print("Votre note est C.")
elif 50 <= Score < 60:
    print("Votre note est D.")
else:
    print("Votre note est E.")

# Vérifions si la saison est l'été, l'hiver, le printemps ou l'automne.
saison = input("(été, hiver, printemps, automne): ").lower()

if saison == "été":
    print("C'est l'été!")
elif saison == "hiver":
    print("C'est l'hiver!")
elif saison == "printemps":
    print("C'est le printemps!")
elif saison == "automne":
    print("C'est l'automne!")
else:
    print("Saison inconnue.")

    # la liste des fruits 

    fruits = ['banana', 'orange', 'mango', 'lemon']

if 'banana' in fruits:
    print("La banane est dans la liste des fruits.")

# Exercice:3

# Liste de Personne

personnes = {'prenom': 'Nathalie', 'Nom_de_famille': 'FIOKOUNA', 'sexe': 'F', 'age': '24', 'pays': 'TOGO', 'ville': 'Lomé','adresse': '123 Rue de l\'Université','situation_matrimoniale': 'Célibataire', 'compétences': ['Python', 'Mathématiques', 'Physique']}

# Vérifions si la personne a des compétences

# imprimons les compétences intermédiaires
if 'Python' in personnes['compétences']:
    print("La personne a des compétences en Python.")


