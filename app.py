from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)
# Load the serialized model
model = joblib.load('Anemia_Diagnosis.pkl')

# Define mapping between encoded values and anemia names
anemia_mapping = {
    0: 'Healthy',
    1: 'Iron deficiency anemia',
    2: 'Leukemia',
    3: 'Leukemia with thrombocytopenia',
    4: 'Macrocytic anemia',
    5: 'Normocytic hypochromic anemia',
    6: 'Normocytic normochromic anemia',
    7: 'Other microcytic anemia',
    8: 'Thrombocytopenia'
}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        input_data = request.json

        if not input_data:
            return jsonify({'error': 'No input data provided'}), 400
        
        # Extract numeric values from the input data
        input_values = [float(value) for value in input_data.values()]
        
        # Perform prediction
        encoded_prediction = model.predict([input_values])[0]
        
        # Map the encoded prediction to the corresponding anemia name
        predicted_anemia = anemia_mapping.get(encoded_prediction, 'Unknown')
        
        # Return the predicted anemia name
        return jsonify({'Result': predicted_anemia})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
