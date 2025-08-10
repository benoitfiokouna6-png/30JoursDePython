def compter_lignes_et_mots(fichier):
    try:
        with open(fichier, 'r') as f:
            lignes = f.readlines()
            nombre_lignes = len(lignes)
            mots = ' '.join(lignes).split()
            nombre_mots = len(mots)
            return nombre_lignes, nombre_mots
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'existe pas.")
        return None

# Fichiers à lire
fichiers = [
    'obama_speech.txt',
    'michelle_obama_speech.txt',
    'donald_speech.txt',
    'melania_trump_speech.txt'
]

for fichier in fichiers:
    result = compter_lignes_et_mots(fichier)
    if result:
        nombre_lignes, nombre_mots = result
        print(f"Fichier : {fichier}")
        print(f"Nombre de lignes : {nombre_lignes}")
        print(f"Nombre de mots : {nombre_mots}")
        print("------------------------")

        import json

def lire_fichier_json(fichier):
    try:
        with open(fichier, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'existe pas.")
        return None

def compter_langues(data):
    langues = {}
    for pays in data:
        for langue in pays['languages']:
            if langue in langues:
                langues[langue] += 1
            else:
                langues[langue] = 1
    return langues

def trouver_dix_langues_les_plus_parlees(langues):
    return sorted(langues.items(), key=lambda x: x[1], reverse=True)[:10]

def main():
    fichier = 'data/Pays_data.json'
    data = lire_fichier_json(fichier)
    if data:
        langues = compter_langues(data)
dix_langues_les_plus_parlees = trouver_dix_langues_les_plus_parlees(langues)
        print("Les dix langues les plus parlées sont :")
        for i, (langue, nombre) in enumerate(dix_langues_les_plus_parlees):
            print(f"{i+1}. {langue} : {nombre} pays")

if __name__ == "__main__":
    main()

import json

def lire_fichier_json(fichier):
    try:
        with open(fichier, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'existe pas.")
        return None

def trouver_dix_pays_les_plus_peuples(data):
    pays_peuples = sorted(data, key=lambda x: x['population'], reverse=True)[:10]
    return [(pays['name'], pays['population']) for pays in pays_peuples]

def main():
    fichier = 'data/Pays_data.json'
    data = lire_fichier_json(fichier)
    
    if data:
        dix_pays_les_plus_peuples = trouver_dix_pays_les_plus_peuples(data)
        print("Les dix pays les plus peuplés sont :")
        for i, (pays, population) in enumerate(dix_pays_les_plus_peuples):
            print(f"{i+1}. {pays} : {population} habitants")

if __name__ == "__main__":
    main()

def extraire_adresses_email(fichier):
    try:
        with open(fichier, 'r') as f:
            texte = f.read()
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            adresses_email = re.findall(pattern, texte)
            return adresses_email
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'existe pas.")
        return None

fichier = 'email_exchange_big.txt'
adresses_email = extraire_adresses_email(fichier)

if adresses_email:
    print("Adresses e-mail extraites :")
    for adresse in adresses_email:
        print(adresse)

import re
from collections import Counter

def find_most_common_words(text_or_file, n):
    if isinstance(text_or_file, str) and '\n' not in text_or_file and '.' in text_or_file:
        try:
            with open(text_or_file, 'r') as f:
                text = f.read().lower()
        except FileNotFoundError:
            print(f"Le fichier {text_or_file} n'existe pas.")
            return None
    else:
        text = text_or_file.lower()

    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    most_common_words = Counter(words).most_common(n)
    return most_common_words

# Test avec une chaîne
text = "This is a test. This test is only a test. If this were a real emergency, you would be instructed to panic."
print(find_most_common_words(text, 5))

# Test avec un fichier
# print(find_most_common_words('fichier.txt', 5))

