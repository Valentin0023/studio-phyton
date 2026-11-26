import asyncio
import httpx
import time

async def prendi_meteo(client, citta, lat, lon):
    dominio = "https://api." + "open-meteo.com"
    url = f"{dominio}/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    risposta = await client.get(url)
    temp = risposta.json()["current_weather"]["temperature"]
    print(f"{citta}: {temp}°C")

async def main():
    inizio = time.time()
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
            prendi_meteo(client, "Roma", 41.90, 12.49),
            prendi_meteo(client, "Milano", 45.46, 9.19),
            prendi_meteo(client, "Napoli", 40.85, 14.26)
        )
    print(f"Fatto tutto in {round(time.time() - inizio, 2)} secondi!")

asyncio.run(main())