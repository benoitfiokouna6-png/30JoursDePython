import math
from collections import Counter

class Statistique:
    def __init__(self, donnees):
        self.donnees = donnees

    def moyenne(self):
        return sum(self.donnees) / len(self.donnees)

    def mediane(self):
        donnees_triees = sorted(self.donnees)
        n = len(donnees_triees)
        if n % 2 == 0:
            return (donnees_triees[n // 2 - 1] + donnees_triees[n // 2]) / 2
        else:
            return donnees_triees[n // 2]

    def mode(self):
        frequences = Counter(self.donnees)
        max_frequence = max(frequences.values())
        modes = [donnee for donnee, frequence in frequences.items() if frequence == max_frequence]
        return modes

    def plage(self):
        return max(self.donnees) - min(self.donnees)

    def variance(self):
        moyenne = self.moyenne()
        return sum((donnee - moyenne) ** 2 for donnee in self.donnees) / len(self.donnees)

    def ecart_type(self):
        return math.sqrt(self.variance())

    def min(self):
        return min(self.donnees)

    def max(self):
        return max(self.donnees)

    def count(self):
        return len(self.donnees)

    def centile(self, p):
        donnees_triees = sorted(self.donnees)
        n = len(donnees_triees)
        return donnees_triees[int(p / 100 * n)]

    def frequence(self):
        frequences = Counter(self.donnees)
        return dict(frequences)

# Exemple d'utilisation
donnees = [1, 2, 3, 4, 4, 5, 5, 5]
statistique = Statistique(donnees)
print("Moyenne :", statistique.moyenne())
print("Médiane :", statistique.mediane())
print("Mode :", statistique.mode())
print("Plage :", statistique.plage())
print("Variance :", statistique.variance())
print("Écart-type :", statistique.ecart_type())
print("Min :", statistique.min())
print("Max :", statistique.max())
print("Count :", statistique.count())
print("25e centile :", statistique.centile(25))
print("75e centile :", statistique.centile(75))
print("Fréquence :", statistique.frequence())

class PersonAccount:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.revenues = []
        self.expenses = []

    def add_income(self, amount, description):
        self.revenues.append({"amount": amount, "description": description})

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})

    def total_income(self):
        return sum(revenu["amount"] for revenu in self.revenues)

    def total_expense(self):
        return sum(expense["amount"] for expense in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return {
            "Nom": f"{self.first_name} {self.last_name}",
            "Revenus totaux": self.total_income(),
            "Dépenses totales": self.total_expense(),
            "Solde du compte": self.account_balance(),
            "Revenus": self.revenues,
"Dépenses": self.expenses
        }

# Exemple d'utilisation
compte = PersonAccount("Jean", "Dupont")
compte.add_income(1000, "Salaire")
compte.add_income(500, "Investissement")
compte.add_expense(800, "Loyer")
compte.add_expense(200, "Nourriture")

print("Informations du compte :", compte.account_info())
print("Solde du compte :", compte.account_balance())
