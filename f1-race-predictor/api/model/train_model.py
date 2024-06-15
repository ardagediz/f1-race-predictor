import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def fetch_training_data():
    # Fetch the data from the Open F1 API
    # This is a placeholder function, replace with actual API calls
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'feature3': [2, 3, 4, 5, 1],
        'target': [1, 0, 1, 0, 1]
    }
    return pd.DataFrame(data)

def train_model():
    # Load your training data
    data = fetch_training_data()
    X = data[['feature1', 'feature2', 'feature3']]
    y = data['target']

    # Train a RandomForest model
    model = RandomForestClassifier()
    model.fit(X, y)

    # Save the trained model
    joblib.dump(model, 'api/model/random_forest_model.joblib')

# Train the model
if __name__ == '__main__':
    train_model()
