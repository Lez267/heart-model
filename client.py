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

response = requests.post(url='https://spotify-model-latest.onrender.com/score',
                         json=body)
print("Respuesta de Render:")
print(response.json())
