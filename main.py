from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from functions.get_formated_data import getFormatedData

from functions.train_model import train_model

app = FastAPI()
class PredictionRequest(BaseModel):
    features: conlist(int, min_length=9, max_length=9)

[testsSamples, samples, targets] = getFormatedData()
perceptron = train_model(samples=samples, targets=targets)
testsPrediction = perceptron.predict(testsSamples)
positivesCount = sum(value == '+1' for value in testsPrediction)
negativesCount = sum(value == '-1' for value in testsPrediction)

@app.post("/predict")
async def predict(request_body: PredictionRequest):
    features = request_body.features
    input_sample = [features]

    prediction = perceptron.predict(input_sample)

    result = 'positivo' if prediction[0] == '+1' else 'negativo'
    return {"prediction": result}

@app.get("/")
async def print():
    return {"message": "Hello World"}

@app.get("/positive-count")
async def getPositiveStatistics():
    return {"message": f"Quantidade de POSITIVOS ENCONTRADA: {positivesCount} x 96 esperado"}

@app.get("/negative-count")
async def getNegativeStatistics():
    return {"message": f"Quantidade de NEGATIVOS ENCONTRADA: {negativesCount} x 96 esperado"}
