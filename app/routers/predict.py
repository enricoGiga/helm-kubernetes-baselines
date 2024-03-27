from fastapi import APIRouter
from app.models.prediction_request import PredictionRequest
import pandas as pd
import joblib
import gzip

router = APIRouter()

model = joblib.load(gzip.open("./data/model_binary.dat.gz", "rb"))


@router.post("/predict")
def predict(request: PredictionRequest):
    data = pd.DataFrame([dict(request)])
    prediction = model.predict(data)

    return {"prediction": int(prediction[0])}
