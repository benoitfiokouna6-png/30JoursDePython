# Spécifiez le chemin du fichier CSV
chemin_fichier = 'donnees/hacker_news.csv'

# Lisez le fichier CSV
df = pd.read_csv(chemin_fichier)

# Chargez le fichier CSV
df = pd.read_csv('hacker_news.csv')

# Affichez les cinq premières lignes
print(df.head(5))

# Chargez le fichier CSV
df = pd.read_csv('hacker_news.csv')

# Affichez les cinq dernières lignes
print(df.tail(5))

# Chargez le fichier CSV
df = pd.read_csv('hacker_news.csv')

# Obtenez la colonne de titre
titre_series = df['title']

# Affichez la série
print(titre_series)

# Chargez le fichier CSV
df = pd.read_csv('hacker_news.csv')

# Comptez le nombre de lignes et de colonnes
print("Nombre de lignes et de colonnes : ", df.shape)

# Filtrez les titres qui contiennent "Python"
titres_python = df[df['title'].str.contains('Python', case=False, na=False)]
print("Titres qui contiennent 'Python' :")
print(titres_python)

# Filtrez les titres qui contiennent "JavaScript"
titres_javascript = df[df['title'].str.contains('JavaScript', case=False, na=False)]
print("Titres qui contiennent 'JavaScript' :")
print(titres_javascript)
