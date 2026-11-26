import httpx 
from bs4 import BeautifulSoup

# Scarichiamo l'HTML di una pagina web di test fatta apposta per lo scraping 
dominio = "https://quotes." + "toscrape.com"
risposta = httpx.get(dominio)

# Trasformiamo l'HTML grezzo in un oggetto navigabile
soup = BeautifulSoup(risposta.text, "html.parser")

#Cerchiamo tutti i blocchi con classe "quote"
citazioni = soup.find_all("div", class_="quote")

for c in citazioni[:3]: # prendiamo solo le prime 3
    testo = c.find("span",class_="text").text
    autore = c.find("small",class_="author").text
    print(f"{autore}: {testo}\n")
    