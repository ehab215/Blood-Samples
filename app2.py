from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved model
model = joblib.load('disease_check.pkl')

# Define the mappings for preprocessing
disease_mapping = {'Acne': 0,
                   'Allergic Rhinitis': 1,
                   "Alzheimer's Disease": 2,
                    'Anemia': 3,
                    'Anxiety Disorders': 4,
                    'Appendicitis': 5,
                    'Asthma': 6,
                    'Atherosclerosis': 7,
                    'Autism Spectrum Disorder (ASD)': 8,
                    'Bipolar Disorder': 9,
                    'Bladder Cancer': 10,
                    'Brain Tumor': 11,
                    'Breast Cancer': 12,
                    'Bronchitis': 13,
                    'Cataracts': 14,
                    'Cerebral Palsy': 15,
                    'Chickenpox': 16,
                    'Cholecystitis': 17,
                    'Cholera': 18,
                    'Chronic Kidney Disease': 19,
                    'Chronic Obstructive Pulmonary Disease (COPD)': 20,
                    'Chronic Obstructive Pulmonary...': 21,
                    'Cirrhosis': 22,
                    'Colorectal Cancer': 23,
                    'Common Cold': 24,
                    'Conjunctivitis (Pink Eye)': 25,
                    'Coronary Artery Disease': 26,
                    "Crohn's Disease": 27,
                    'Cystic Fibrosis': 28,
                    'Dementia': 29,
                    'Dengue Fever': 30,
                    'Depression': 31,
                    'Diabetes': 32,
                    'Diverticulitis': 33,
                    'Down Syndrome': 34,
                    'Eating Disorders (Anorexia,...': 35,
                    'Ebola Virus': 36,
                    'Eczema': 37,
                    'Endometriosis': 38,
                    'Epilepsy': 39,
                    'Esophageal Cancer': 40,
                    'Fibromyalgia': 41,
                    'Gastroenteritis': 42,
                    'Glaucoma': 43,
                    'Gout': 44,
                    'HIV/AIDS': 45,
                    'Hemophilia': 46,
                    'Hemorrhoids': 47,
                    'Hepatitis': 48,
                    'Hepatitis B': 49,
                    'Hyperglycemia': 50,
                    'Hypertension': 51,
                    'Hypertensive Heart Disease': 52,
                    'Hyperthyroidism': 53,
                    'Hypoglycemia': 54,
                    'Hypothyroidism': 55,
                    'Influenza': 56,
                    'Kidney Cancer': 57,
                    'Kidney Disease': 58,
                    'Klinefelter Syndrome': 59,
                    'Liver Cancer': 60,
                    'Liver Disease': 61,
                    'Lung Cancer': 62,
                    'Lyme Disease': 63,
                    'Lymphoma': 64,
                    'Malaria': 65,
                    'Marfan Syndrome': 66,
                    'Measles': 67,
                    'Melanoma': 68,
                    'Migraine': 69,
                    'Multiple Sclerosis': 70,
                    'Mumps': 71,
                    'Muscular Dystrophy': 72,
                    'Myocardial Infarction (Heart...': 73,
                    'Obsessive-Compulsive Disorde...': 74,
                    'Osteoarthritis': 75,
                    'Osteomyelitis': 76,
                    'Osteoporosis': 77,
                    'Otitis Media (Ear Infection)': 78,
                    'Ovarian Cancer': 79,
                    'Pancreatic Cancer': 80,
                    'Pancreatitis': 81,
                    "Parkinson's Disease": 82,
                    'Pneumocystis Pneumonia (PCP)': 83,
                    'Pneumonia': 84,
                    'Pneumothorax': 85,
                    'Polio': 86,
                    'Polycystic Ovary Syndrome (PCOS)': 87,
                    'Prader-Willi Syndrome': 88,
                    'Prostate Cancer': 89,
                    'Psoriasis': 90,
                    'Rabies': 91,
                    'Rheumatoid Arthritis': 92,
                    'Rubella': 93,
                    'Schizophrenia': 94,
                    'Scoliosis': 95,
                    'Sepsis': 96,
                    'Sickle Cell Anemia': 97,
                    'Sinusitis': 98,
                    'Sleep Apnea': 99,
                    'Spina Bifida': 100,
                    'Stroke': 101,
                    'Systemic Lupus Erythematosus...': 102,
                    'Testicular Cancer': 103,
                    'Tetanus': 104,
                    'Thyroid Cancer': 105,
                    'Tonsillitis': 106,
                    'Tourette Syndrome': 107,
                    'Tuberculosis': 108,
                    'Turner Syndrome': 109,
                    'Typhoid Fever': 110,
                    'Ulcerative Colitis': 111,
                    'Urinary Tract Infection': 112,
                    'Urinary Tract Infection (UTI)': 113,
                    'Williams Syndrome': 114,
                    'Zika Virus': 115}
fever_mapping = {'No': 0, 'Yes': 1}
cough_mapping = {'No': 0, 'Yes': 1}
fatigue_mapping = {'No': 0, 'Yes': 1}
difficulty_breathing_mapping = {'No': 0, 'Yes': 1}
gender_mapping = {'Female': 0, 'Male': 1}
blood_pressure_mapping = {'Low': 1, 'Normal': 2, 'High': 0}
cholesterol_level_mapping = {'Low': 1, 'Normal': 2, 'High': 0}

def preprocess_input(input_data):
    # Convert actual values to encoded values
    input_data['Disease'] = disease_mapping[input_data['Disease']]
    input_data['Fever'] = fever_mapping[input_data['Fever']]
    input_data['Cough'] = cough_mapping[input_data['Cough']]
    input_data['Fatigue'] = fatigue_mapping[input_data['Fatigue']]
    input_data['Difficulty Breathing'] = difficulty_breathing_mapping[input_data['Difficulty Breathing']]
    input_data['Gender'] = gender_mapping[input_data['Gender']]
    input_data['Blood Pressure'] = blood_pressure_mapping[input_data['Blood Pressure']]
    input_data['Cholesterol Level'] = cholesterol_level_mapping[input_data['Cholesterol Level']]
    
    return pd.DataFrame([input_data])

def make_prediction(input_data):
    # Preprocess the input data
    preprocessed_data = preprocess_input(input_data)
    
    # Make prediction
    prediction = model.predict(preprocessed_data)
    
    # Map the prediction to the actual outcome
    outcome_mapping = {0: 'Negative', 1: 'Positive'}
    
    return outcome_mapping[prediction[0]]

@app.route('/check', methods=['POST'])
def predict():
    input_data = request.json
    try:
        result = make_prediction(input_data)
        if result == "Negative":
            return jsonify({'Be happy your result is': result}), 200
        else:
            return jsonify({'We are so sorry, your result is': result}), 200
    except Exception as e:
        print("Sorry, There is an error, we will fix it soon")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
