import pandas as pd
import pathlib
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from joblib import dump

print('Loading dataset...')
df = pd.read_csv(pathlib.Path('data/spotify.csv'))

cols_to_use = [
    'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness', 'valence',
    'tempo', 'duration_ms'
]

X = df[cols_to_use]
y = df['track_popularity']

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

print('Training XGBoost model...')
my_model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.05,
    n_jobs=4,
    random_state=42
)
my_model.fit(X_train, y_train)

print('Saving model...')
pathlib.Path('model').mkdir(exist_ok=True)
dump(my_model, pathlib.Path('model/spotify-model-v1.joblib'))
print('Model trained and saved successfully!')
