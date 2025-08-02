import math

# Exercice : 1

# déclarations d'une fontion 

def add_two_numbers(1 , 2) # code de la fonction add_two_numbers

# écrivons une fonctions calculans la zone du crecle 

# zone = pi*r*r

def calculer_cercle

zone = math.pi * (r**2)

def add_all_nums(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
    return total

# écrivons une fonction qui peut converti °C °F converti celsuis to fahrenheit

 °F = (°C X 9/5 ) + 32

 def celsuis_en_fahrenheit(celsuis) : fahrenheit = (celsuis * 9/5) + 32

     return  fahrenheit 

    celsuis = float(input("30 :") )


    fahrenheit = celsuis_en_fahrenheit(celsuis)

    print(f"{30}°C) est egal a {fahrenheit:.2f}°F") # la temperature en celsuis est 30 30.0°C est égal a 86.00°F

    def check_season(mois):

        if mois in [12, 1, 2]:
          return "hiver
        elif mois in [3, 4, 5]:  

         return "printemps"
        elif mois in [6, 7, 8]:
         return "été"

def calcul_slope:() m = (y2-y1)/(x2-X1) # (X1,y1) et (X2,y2)sont deux points sur la ligne

def evens_and_odds(n):
    n = int("input 5:")

    n = evens_and_odds(n)
    fonctions(n)
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

        def are_all_elements_unique(lst):
            return len(lst) == len(set(lst))

def verifier_type(liste) :
    if not liste:
        return True
        type_donnees = type(liste[0])
        for element in liste :
            if not isinstance(element,type_donnees):
                                                    return False 
                                                return True

 # écrivons une fonctions qui vrifie si la rariable fournie est une variable python valide

 def est_variable_valide(nom_variable):
    if not 

 isinstance(nom_variable, str):
         return False
    if not 
 nom_variable.isidentifier():
     if

     keyword.iskeyword(nom_variable):
            return False 
            return  True                                                      

            

