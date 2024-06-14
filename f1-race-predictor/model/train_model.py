import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Example data loading and preprocessing
data = pd.read_csv('data.csv')
X = data[['feature1', 'feature2', 'feature3']]
y = data['target']

# Train the model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save the model
joblib.dump(model, 'model/f1_race_predictor.pkl')
