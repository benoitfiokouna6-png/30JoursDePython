import requests
from collections import Counter
import re

def trouver_mots_frequents(url, n):
    response = requests.get(url)
    texte = response.text.lower()
    texte = re.sub(r'[^\w\s]', '', texte)
    mots = texte.split()
    frequences = Counter(mots).most_common(n)
    return frequences

url = 'http://www.gutenberg.org/files/1112/1112.txt'
n = 10
mots_frequents = trouver_mots_frequents(url, n)

print("Les 10 mots les plus fréquents dans Roméo et Juliette sont :")
for mot, frequence in mots_frequents:
    print(f"{mot} : {frequence}")
# Les 10 mots les plus fréquents dans Roméo et Juliette sont :
the : 783
and : 645
to : 542
of : 535
a : 453
i : 434
that : 364
is : 357
in : 346
my : 335

import requests
import statistics

# Requête API
response = requests.get('https://api.thecatapi.com/v1/breeds')
data = response.json()

# Calcul des statistiques sur le poids
weights = []
for breed in data:
    weight = breed['weight']['metric'].split(' - ')
    weights.append((int(weight[0]) + int(weight[1])) / 2)

min_weight = min([int(breed['weight']['metric'].split(' - ')[0]) for breed in data])
max_weight = max([int(breed['weight']['metric'].split(' - ')[1]) for breed in data])
mean_weight = statistics.mean(weights)
median_weight = statistics.median(weights)

# Calcul des statistiques sur la durée de vie
life_spans = []
for breed in data:
    life_span = breed['life_span'].split(' - ')
    life_spans.append((int(life_span[0]) + int(life_span[1])) / 2)

min_life_span = min([int(breed['life_span'].split(' - ')[0]) for breed in data])
max_life_span = max([int(breed['life_span'].split(' - ')[1]) for
mean_life_span = statistics.mean(life_spans)
median_life_span = statistics.median(life_spans)

# Création du tableau de fréquence de pays et de race de chats
country_breeds = {}
for breed in data:
    country = breed['origin']
    if country in country_breeds:
        country_breeds[country].append(breed['name'])
    else:
        country_breeds[country] = [breed['name']]

print("Poids minimum :", min_weight)
print("Poids maximum :", max_weight)
print("Poids moyen :", mean_weight)
print("Médiane du poids :", median_weight)

print("Durée de vie minimum :", min_life_span)
print("Durée de vie maximum :", max_life_span)
print("Durée de vie moyenne :", mean_life_span)
print("Médiane de la durée de vie :", median_life_span)

print("Tableau de fréquence de pays et de race de chats :")
for country, breeds in country_breeds.items():
    print(country, ":", breeds)

import requests

# API des pays (remplacer par l'API spécifique)
url = "https://restcountries.com/v3.1/all"

response = requests.get(url)
data = response.json()

# Récupérer les langues
langues = []
for pays in data:
    for langue in pays['languages']:
        langues.append(langue)

# Compter les langues uniques
langues_uniques = set(langues)
print(f"Nombre de langues uniques : {len(langues_uniques)}")

import requests
from bs4 import BeautifulSoup

url = "https://archive.ics.uci.edu/ml/datasets.php"

# Envoi d'une requête GET à l'URL
response = requests.get(url)

# Vérification si la requête a réussi
if response.status_code == 200:
    # Parsing du contenu HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraction des informations souhaitées
    datasets = soup.find_all('tr')

    for dataset in datasets:
        # Extraction du nom du dataset
        nom_dataset = dataset.find('a')
        if nom_dataset:
            print(nom_dataset.text.strip())

        # Extraction de la description du dataset
        description = dataset.find('td')
        if description:
            print(description.text.strip())
else:
    print("Échec de la requête")
