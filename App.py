import pickle
import streamlit as st # type: ignore
import numpy as np # type: ignore
import pickle # type: ignore

# Load trained model
try:
    model = pickle.load(open('cervical_cancer_model.pkl', 'rb'))
except:
    st.error("Model file not found. Please train and save the model as 'cervical_cancer_model.pkl'")

# App title
st.title("Cervical Cancer Prediction")
st.write("Enter patient details to predict the likelihood of cervical cancer.")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
num_sexual_partners = st.number_input("Number of Sexual Partners", min_value=0, max_value=20, value=1)
first_sexual_intercourse = st.number_input("Age at First Intercourse", min_value=10, max_value=50, value=18)
pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=1)
smokes = st.radio("Do you Smoke?", ('No', 'Yes'))
smokes = 1 if smokes == 'Yes' else 0
hormonal_contraceptives = st.radio("Using Hormonal Contraceptives?", ('No', 'Yes'))
hormonal_contraceptives = 1 if hormonal_contraceptives == 'Yes' else 0
stds = st.radio("Have you had any STDs?", ('No', 'Yes'))
stds = 1 if stds == 'Yes' else 0

# Predict Button
if st.button("Predict"):
    # Prepare input data
    features = np.array([[age, num_sexual_partners, first_sexual_intercourse, pregnancies, smokes, hormonal_contraceptives, stds]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("High Risk of Cervical Cancer. Please consult a doctor.")
    else:
        st.success("Low Risk of Cervical Cancer. Stay Healthy!")

st.write("**Disclaimer:** This prediction is for informational purposes only and not a substitute for professional medical advice.")
