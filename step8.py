import httpx

dominio = "https://api." + "open-meteo.com"
url = dominio + "/v1/forecast?latitude=41.90&longitude=12.49&current_weather=true"

risposta = httpx.get(url)
dati = risposta.json()

temperatura = dati["current_weather"]["temperature"]
vento = dati["current_weather"]["windspeed"]

print(f"A Roma ora ci sono {temperatura}°C con vento a {vento} km/h!")