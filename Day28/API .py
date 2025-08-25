url = "https://api.example.com/data"
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print("Erreur :", response.status_code)

url = "https://api.example.com/data"
data = {"nom": "John", "age": 30}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("Données envoyées avec succès")
else:
    print("Erreur :", response.status_code)
