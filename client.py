import requests

body = {
    "danceability": 0.651,
    "energy": 0.800,
    "key": 1.0,
    "loudness": -5.359,
    "mode": 1.0,
    "speechiness": 0.1,
    "acousticness": 0.2,
    "instrumentalness": 0.0,
    "liveness": 0.1,
    "valence": 0.5,
    "tempo": 120.0,
    "duration_ms": 200000.0
}

# Reemplaza con la URL de tu servicio en Render (ejemplo: https://heart-model-xxxx.onrender.com/score)
response = requests.post(url='http://localhost:80/score', json=body)
print("Respuesta del modelo:")
print(response.json())
