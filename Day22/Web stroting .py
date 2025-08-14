import request 
from bs4 import BeautifulSoup
import json

url = "https://www.bu.edu"

# Envoi d'une requête GET à l'URL
response = requests.get(url)

# Vérification si la requête a réussi
if response.status_code == 200:
    # Parsing du contenu HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraction des données
    donnees = {
        "faits_et_statistiques": {
            "depenses_de_recherche": "$554.0M",
            "programmes_d_etude_a_l_etranger": "200+",
            "bourses_de_recherche": "$645.6M",
            "communaute": {
                "etudiants": 37701,
                "anciens_etudiants": 431000,
                "employes": 10674,
                "professeurs": 4309
            },
            "campus": {
                "salles_de_classe": 848,
                "batiments": 343,
                "laboratoires": 1481,
                "bibliotheques": 13,
                "superficie_du_campus": "140 acres"
            },
            "academiques": {
                "programmes_d_etude_a_l_etranger": "80+",
                "taille_moyenne_des_classes": 30,
                "professeurs": 4309,
                "ratio_etudiants_professeurs": "11:1",
                "ecoles_et_colleges": 17,
                "programmes_d_etudes": "300+"
            }
        }
    }

    # Stockage des données dans un fichier JSON
    with open('donnees_bu.json', 'w') as fichier:
        json.dump(donnees, fichier, indent=4)

    print("Données stockées dans donnees_bu.json")
else:
    print("Échec de la requête")

import requests
from bs4 import BeautifulSoup
import json

url = "https://archive.ics.uci.edu/ml/index.php"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extraction des datasets populaires
datasets_populaires = []
for item in soup.find_all('h2'):
    if item.text.strip() == "Popular Datasets":
        datasets = item.find_next('ul').find_all('li')
        for dataset in datasets:
            datasets_populaires.append(dataset.text.strip())

# Création du dictionnaire de données
donnees = {
    "datasets_populaires": datasets_populaires
}

# Stockage des données dans un fichier JSON
with open('donnees_uci.json', 'w') as fichier:
    json.dump(donnees, fichier, indent=4)

print("Données stockées dans donnees_uci.json")


import json

# Liste des présidents avec leurs informations
presidents = [
    {"nom": "George Washington", "parti": "Indépendant", "mandat": "1789-1797"},
    {"nom": "John Adams", "parti": "Fédéraliste", "mandat": "1797-1801"},
    {"nom": "Thomas Jefferson", "parti": "Démocrate-Républicain", "mandat": "1801-1809"},
    {"nom": "James Madison", "parti": "Démocrate-Républicain", "mandat": "1809-1817"},
    {"nom": "James Monroe", "parti": "Démocrate-Républicain", "mandat": "1817-1825"},
    {"nom": "John Quincy Adams", "parti": "Démocrate-Républicain / National Républicain", "mandat": "1825-1829"},
    {"nom": "Andrew Jackson", "parti": "Démocrate", "mandat": "1829-1837"},
    {"nom": "Martin Van Buren", "parti": "Démocrate", "mandat": "1837-1841"},
    {"nom": "William Henry Harrison", "parti": "Whig", "mandat": "1841"},
    {"nom": "John Tyler", "parti": "Whig / Indépendant", "mandat": "1841-1845"},
    {"nom": "James K. Polk", "parti": "Démocrate", "mandat": "1845-1849"},
    {"nom": "Zachary Taylor", "parti": "Whig", "mandat": "1849-1850"},
    {"nom": "Millard Fillmore", "parti": "Whig", "mandat": "1850-1853"},
    {"nom": "Franklin Pierce", "parti": "Démocrate", "mandat": "1853-1857"},
    {"nom": "James Buchanan", "parti": "Démocrate", "mandat": "1857-1861"},
    {"nom": "Abraham Lincoln", "parti": "Républicain", "mandat": "1861-1865"},
    {"nom": "Andrew Johnson", "parti": "Démocrate / National Union", "mandat": "1865"}]

