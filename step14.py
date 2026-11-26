import mongomock 

# 1. Apri il database e la cartella (collezione) "candidati"
db = mongomock.MongoClient()["lavoro"]
candidati = db["candidati"]

# 2. Salva due schede (nota che hanno campi diversi!)
candidati.insert_one({"nome": "Marco", "skill": ["Python", "SQL"]})
candidati.insert_one({"nome": "Sara", "skill": ["Java", "AWS"], "citta": "Milano"})

# 3. Cerca chi sa "Python"
for persona in candidati.find({"skill": "Python"}):
    print("Trovato:", persona["nome"])

