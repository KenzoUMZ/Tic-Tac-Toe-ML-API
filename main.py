from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import LabelEncoder
import pandas as pd

from functions.train_perceptron import train_perceptron

app = FastAPI()


# Define a Pydantic model to specify the JSON request body structure

# Modify the Pydantic model to specify the expected number of features
class PredictionRequest(BaseModel):
    features: conlist(int, min_length=27, max_length=27)  # Assuming you expect 27 features


# Train the perceptron when the application starts
perceptron = train_perceptron('tic_tac_toe.csv')


# Define the prediction endpoint
@app.post("/predict")
async def predict(request_body: PredictionRequest):
    # Extract the features from the request body
    features = request_body.features

    # Convert the input features to a numpy array (assuming one-hot encoding is done)
    input_features = [features]  # Convert to list of lists

    # Make a prediction using the trained perceptron
    prediction = perceptron.predict(input_features)

    # Map the numerical prediction back to labels
    result = 'positivo' if prediction[0] == 1 else 'negativo'

    return {"prediction": result}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
