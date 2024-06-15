import React, { useState } from 'react';
import './App.css';

function App() {
    const [prediction, setPrediction] = useState(null);

    const handlePredict = async () => {
        const feature1 = document.getElementById('feature1').value;
        const feature2 = document.getElementById('feature2').value;
        const feature3 = document.getElementById('feature3').value;

        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ feature1, feature2, feature3 }),
        });
        const data = await response.json();
        setPrediction(data.prediction);
    };

    return (
        <div className="App">
            <h1>F1 Race Predictor</h1>
            <div>
                <input type="number" id="feature1" placeholder="Feature 1" />
                <input type="number" id="feature2" placeholder="Feature 2" />
                <input type="number" id="feature3" placeholder="Feature 3" />
                <button onClick={handlePredict}>Predict</button>
            </div>
            {prediction && <div id="result">Prediction: {prediction}</div>}
        </div>
    );
}

export default App;
