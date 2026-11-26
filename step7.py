import json

offerte_trovate = [
    {"ruolo": "Python Dev", "ral": 30000},
    {"ruolo": "AI Engineer", "ral": 35000},
    {"ruolo": "Java Dev", "ral": 28000}
]

# 1. Salva i dati in un vero file JSON sul PC
with open("offerte.json", "w", encoding="utf-8") as file:
    json.dump(offerte_trovate, file, indent=4)

print("File offerte.json creato!")

# 2. Rilegge i dati dal file appena creato
with open("offerte.json", "r", encoding="utf-8") as file:
    dati_letti = json.load(file)

print("Primo ruolo letto dal file:", dati_letti[0]["ruolo"])
print("Ultimo ruolo letto dal file:", dati_letti[2]["ruolo"])
