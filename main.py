from fastapi import FastAPI
from pydantic import BaseModel, conlist
from functions.get_formated_data import getFormatedData

from functions.train_model import train_model

app = FastAPI()
class PredictionRequest(BaseModel):
    features: conlist(int, min_length=9, max_length=9)

[testsSamples, samples, targets] = getFormatedData()
perceptron = train_model(samples=samples, targets=targets)
testsPrediction = perceptron.predict(testsSamples)

print('\n\nQUANTIDADE DE AMOSTRAS UTILIZADAS PARA TESTAR O MODELO::::', len(testsSamples))
positivesCount = sum(value == '+1' for value in testsPrediction)
negativesCount = sum(value == '-1' for value in testsPrediction)

@app.post("/predict")
async def predict(request_body: PredictionRequest):
    features = request_body.features
    input_sample = [features]

    prediction = perceptron.predict(input_sample)

    result = 'sim' if prediction[0] == '+1' else 'nao'
    return {"prediction": result}

@app.get("/")
async def print():
    return {"message": "Hello World"}

@app.get("/positive-count")
async def getPositiveStatistics():
    return {"message": f"Vitórias de X encontradas {positivesCount} x 96 esperado"}

@app.get("/negative-count")
async def getNegativeStatistics():
    return {"message": f"Quantidades de vezes que x não venceu {negativesCount} x 96 esperado"}
