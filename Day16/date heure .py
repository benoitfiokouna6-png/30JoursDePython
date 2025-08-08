from datetime import datetime

# Obtenir la date et l'heure actuelles
now = datetime.now()

# Obtenir le jour en cours
jour = now.day
print(f"Jour : {jour}")

# Obtenir le mois
mois = now.month
print(f"Mois : {mois}")

# Obtenir l'année
annee = now.year
print(f"Année : {annee}")

# Obtenir l'heure
heure = now.hour
print(f"Heure : {heure}")

# Obtenir la minute
minute = now.minute
print(f"Minute : {minute}")

# Obtenir l'horodatage
horodatage = now.timestamp()
print(f"Horodatage : {horodatage}")

# Afficher la date et l'heure dans un format lisible

print(f"Date et heure : {now.strftime('%Y-%m-%d %H:%M:%S')}")

from datetime import datetime

# Obtenir la date et l'heure actuelles
now = datetime.now()

# Formater la date et l'heure
date_formatee = now.strftime("%m/%d/%y, %H:%M:%S")
print(date_formatee)

from datetime import datetime

# Définir la date actuelle
date_actuelle = datetime(2019, 12, 5)

# Afficher la date actuelle
print("Date actuelle : ", date_actuelle.strftime("%d/%m/%Y"))

# Changer la période de temps
nouvelle_date = date_actuelle.replace(year=2022, month=6, day=15)

# Afficher la nouvelle date
print("Nouvelle date : ", nouvelle_date.strftime("%d/%m/%Y"))

# Définir la date actuelle
date_actuelle = datetime.now()

# Définir la date de la nouvelle année
nouvelle_annee = datetime(date_actuelle.year + 1, 1, 1)

# Calculer le décalage horaire
decalage_horaire = nouvelle_annee - date_actuelle

# Afficher le décalage horaire
jours = decalage_horaire.days
heures = decalage_horaire.seconds // 3600
minutes = (decalage_horaire.seconds // 60) % 60
secondes = decalage_horaire.seconds % 60

print(f"Décalage horaire jusqu'à la nouvelle année : {jours} jours, {heures} heures, {minutes} minutes et {secondes} secondes")

# Définir la date de référence (1er janvier 1970)
date_reference = datetime(1970, 1, 1)

# Définir la date actuelle
date_actuelle = datetime.now()

# Calculer le décalage horaire
decalage_horaire = date_actuelle - date_reference

# Afficher le décalage horaire
jours = decalage_horaire.days
heures = decalage_horaire.seconds // 3600
minutes = (decalage_horaire.seconds // 60) % 60
secondes = decalage_horaire.seconds % 60

print(f"Décalage horaire depuis le 1er janvier 1970 : {jours} jours, {heures} heures, {minutes} minutes et {secondes} secondes")

# nous utilisons le module Date Time pour analyser des séries chronologiques  , pour obtenir un horodages de toutes les activités dans une appliaton 

