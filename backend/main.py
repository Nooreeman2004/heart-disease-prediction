from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

# Initialize FastAPI app
app = FastAPI(title="Heart Disease Prediction API", description="Predict heart disease using a trained model", version="1.0")

# Define the input schema
class HeartDiseaseInput(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# Define the prediction endpoint
@app.post("/predict", summary="Predict Heart Disease", description="Send patient data to predict the likelihood of heart disease.")
def predict(input_data: HeartDiseaseInput):
    # Convert input to model-ready format
    data = np.array([[
        input_data.age, input_data.sex, input_data.cp,
        input_data.trestbps, input_data.chol, input_data.fbs,
        input_data.restecg, input_data.thalach, input_data.exang,
        input_data.oldpeak, input_data.slope, input_data.ca, input_data.thal
    ]])
    
    # Make prediction
    prediction = model.predict(data)
    prediction_proba = model.predict_proba(data).max(axis=1)

    return {
        "prediction": int(prediction[0]),
        "confidence": float(prediction_proba[0])
    }

# Root endpoint
@app.get("/")
def root():
    return {"message": "Heart Disease Prediction API is live! Navigate to /docs for Swagger UI."}