import requests

body = {
    "age": 94,
    "sex": 1,
    "cp": 3,
    "trestbps": 140,
    "chol": 320,
    "fbs": 0,
    "restecg": 0,
    "thalach": 199,
    "exang": 1,
    "oldpeak": 1.8,
    "slope": 1,
    "ca": 2,
    "thal": 2
}

# Reemplaza con la URL pública de tu Web Service en Render
# Ejemplo: https://heart-model-xxxx.onrender.com/score
response = requests.post(url='http://localhost:80/score',
                         json=body)
print(response.json())
