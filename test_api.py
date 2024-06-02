# test_api.py

import requests

# Example JSON data for prediction
data = {
    "cement": 300,
    "slag": 0,
    "fly_ash": 0,
    "water": 180,
    "superplasticizer": 0,
    "coarse_aggregate": 1037,
    "fine_aggregate": 100,
    "age": 7
}

# URL of the predict endpoint
url = 'http://127.0.0.1:5000/predict'

# Send POST request to the predict endpoint with JSON data
response = requests.post(url, json=data)

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Print the predicted compressive strength
    print("Predicted Compressive Strength:", response.json()['compressive_strength'])
else:
    print("Error:", response.text)
