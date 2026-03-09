import requests

# Define the URL of the prediction endpoint
url = 'http://127.0.0.1:8080/predict'

# Sample input data (replace with your own data)
input_data = {
    "WBC": 10,
    "LYMp": 43.2,
    "NEUTp": 50.1,
    "LYMn": 4.3,
    "NEUTn": 6,
    "RBC": 2.77,
    "HGB": 7.3,
    "HCT": 24.2,
    "MCV": 87.7,
    "MCH":26.3,
    "MCHC": 30.1,
    "PLT": 189,
    "PDW": 12.2,
    "PCT": 0.17

    # Add more features as needed
}
input_data2 = {
    "WBC": 10,
    "LYMp": 10,
    "NEUTp": 10,
    "LYMn": 10,
    "NEUTn": 10,
    "RBC": 10,
    "HGB": 10,
    "HCT": 10,
    "MCV": 10,
    "MCH": 10,
    "MCHC": 10,
    "PLT": 10,
    "PDW": 10,
    "PCT": 10


    # Add more features as needed
}


# Send a POST request to the prediction endpoint with the input data
response = requests.post(url, json=input_data)
response2 = requests.post(url, json=input_data2)

# Print the response
print(response.json())
print(response2.json())
