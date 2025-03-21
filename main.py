from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model/intrusion_model.pkl")

@app.post("/predict/")
async def predict(features: list):
    prediction = model.predict(np.array(features).reshape(1, -1))
    return {"intrusion_detected": bool(prediction[0])}
