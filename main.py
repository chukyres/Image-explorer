import requests

##api = KZye7kp423u3SBROBgEQzM1htDynd6iZeCU8EDU9

API_KEY = "KZye7kp423u3SBROBgEQzM1htDynd6iZeCU8EDU9"

url = "https://api.nasa.gov/planetary/apod"

params = {
    "api_key": API_KEY,
    "start_date": "2026-01-01",
    "end_date": "2026-01-05"
}

respuesta = requests.get(url, params=params)
datos = respuesta.json()

for imagen in datos:
    print(imagen["date"], "-", imagen["title"], "\n")
    print(imagen["url"], "\n")
    print("Explicación:", imagen["explanation"], "\n")