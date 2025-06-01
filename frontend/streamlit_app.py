import streamlit as st
import requests

st.title("Heart Disease Prediction")

# Input fields for features your model expects
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x==0 else "Male")
cp = st.selectbox("Chest Pain Type (cp)", options=[0,1,2,3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200, value=120)
chol = st.number_input("Cholesterol (chol)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1])
restecg = st.selectbox("Resting ECG Results (restecg)", options=[0,1,2])
thalach = st.number_input("Max Heart Rate Achieved (thalach)", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", options=[0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of ST Segment (slope)", options=[0,1,2])
ca = st.selectbox("Number of Major Vessels (ca)", options=[0,1,2,3,4])
thal = st.selectbox("Thalassemia (thal)", options=[0,1,2,3])

if st.button("Predict"):
    data = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }

    # Your FastAPI URL, adjust if deployed or port changed
    url = "http://127.0.0.1:8000/predict"

    response = requests.post(url, json=data)
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        st.success(f"Prediction: {'Heart Disease Detected' if prediction == 1 else 'No Heart Disease Detected'}")
    else:
        st.error("Error getting prediction. Try again.")
