offerte_lavoro = [
    {"ruolo": "Python Dev", "remoto": True, "ral": 30000},
    {"ruolo": "Java Dev", "remoto": False, "ral": 28000},
    {"ruolo": "AI Engineer", "remoto": True, "ral": 35000}
]

def filtra_remoto(lista_offerte):
    for offerta in lista_offerte:
        if offerta["remoto"] == True and offerta["ral"] > 30000:
            print(f"Trovata offerta 100% remoto: {offerta['ruolo']} - {offerta['ral']}€")

filtra_remoto(offerte_lavoro)
