from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('concrete_strength_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return "Welcome to the Concrete Strength Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [data['cement'], data['slag'], data['fly_ash'], data['water'], data['superplasticizer'], data['coarse_aggregate'], data['fine_aggregate'], data['age']]
    features = scaler.transform([features])
    prediction = model.predict(features)
    return jsonify({'compressive_strength': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
