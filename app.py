import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("income_model.pkl", "rb"))

st.title("💰 Adult Income Prediction App")

# Collect user input
age = st.number_input("Age", min_value=17, max_value=100, value=25)
education_num = st.number_input("Education Number", min_value=1, max_value=16, value=10)
hours_per_week = st.number_input("Hours per Week", min_value=1, max_value=100, value=40)
capital_gain = st.number_input("Capital Gain", min_value=0, value=0)
capital_loss = st.number_input("Capital Loss", min_value=0, value=0)

# Simple numeric input version
if st.button("Predict"):
    # Arrange input data (⚠️ adjust order of features to match training)
    input_data = np.array([[age, education_num, hours_per_week, capital_gain, capital_loss]])
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("🎉 Income is likely >50K")
    else:
        st.warning("💼 Income is likely <=50K")
