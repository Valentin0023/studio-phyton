class OffertaLavoro:
    def __init__(self, ruolo, azienda, ral, remoto):
        self.ruolo = ruolo 
        self.azienda = azienda 
        self.ral = ral 
        self.remoto = remoto

    def descrivi(self):
        tipo = "Full Remote" if self.remoto else "In Sede"
        return f"{self.ruolo} presso {self.azienda} ({tipo}) - {self.ral}€"

    def is_ben_pagata(self):
        return self.ral >= 30000

offerta1 = OffertaLavoro("Python AI Dev", "TechItalia", 34000, True)
offerta2 = OffertaLavoro("Junior Web", "StudioWeb", 24000, False)

print(offerta1.descrivi())
print("Ben pagata?", offerta1.is_ben_pagata())
print(offerta2.descrivi())
print("Ben pagata?", offerta2.is_ben_pagata())
