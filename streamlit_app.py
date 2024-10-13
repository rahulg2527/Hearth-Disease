import streamlit as st
from joblib import load
import pandas as pd

# Load your model
try:
    loaded_model = load(filename='heart_disease_model.joblib')
except Exception as e:
    st.error(body=f"Error loading model: {e}")

# Define a function to make predictions
def predict_heart_disease(sample_patient_features):
    try:
        input_df = pd.DataFrame([sample_patient_features])
        prediction = loaded_model.predict(input_df)
        return prediction[0]
    except Exception as e:
        st.error(body=f"Prediction failed: {e}")

# Streamlit UI components
st.title(body="Heart Disease Prediction App")

# User inputs
age = st.number_input(label="Age", min_value=1, max_value=120)
sex = st.selectbox(label="Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.number_input(label="Chest Pain Type (0-3)", min_value=0, max_value=3)
trestbps = st.number_input(label="Resting Blood Pressure (mm Hg)", min_value=0)
chol = st.number_input(label="Cholesterol (mg/dl)", min_value=0)
fbs = st.selectbox(label="Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
restecg = st.number_input(label="Resting Electrocardiographic Results (0-2)", min_value=0, max_value=2)
thalach = st.number_input(label="Maximum Heart Rate Achieved", min_value=0)
exang = st.selectbox(label="Exercise Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
oldpeak = st.number_input(label="Oldpeak", min_value=0.0, step=0.1)
slope = st.number_input(label="Slope of the Peak Exercise ST Segment (0-2)", min_value=0, max_value=2)
ca = st.number_input(label="Number of Major Vessels (0-3)", min_value=0, max_value=3)
thal = st.number_input(label="Thalassemia (0-3)", min_value=0, max_value=3)

# Button to make prediction
if st.button("Predict"):
    sample_patient_features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    result = predict_heart_disease(sample_patient_features=sample_patient_features)
    if result == 1:
        st.success(body="The patient is predicted to have heart disease.")
    else:
        st.success(body="The patient is not predicted to have heart disease.")
