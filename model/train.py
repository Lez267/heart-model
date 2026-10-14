from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
from joblib import dump
import pandas as pd
import pathlib

df = pd.read_csv(pathlib.Path('data/spotify.csv'))

cols_to_use = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
               'acousticness', 'instrumentalness', 'liveness', 'valence',
               'tempo', 'duration_ms']

X = df[cols_to_use]
y = df['track_popularity']

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=0)

print('Training model..')
my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=4,
                        early_stopping_rounds=5)
my_model.fit(X_train, y_train,
             eval_set=[(X_valid, y_valid)],
             verbose=False)

predictions = my_model.predict(X_valid)
print('MAE:', mean_absolute_error(predictions, y_valid))

print('Saving model..')
dump(my_model, pathlib.Path('model/spotify-model-v1.joblib'))
