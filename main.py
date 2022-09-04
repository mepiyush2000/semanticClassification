from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
app = FastAPI()

@app.post('/predict')
async def predict_species():

    dgh = SentimentPrediction()
    pred = dgh.predict(["hi"], model, tokenizer_)
    return {
        'prediction': pred
    }