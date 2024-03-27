import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.prediction_request import PredictionRequest

client = TestClient(app)

def test_predict():
    # Define some example data
    data = PredictionRequest(
        concavity_mean=0.1,
        concave_points_mean=0.05,
        perimeter_se=75,
        area_se=500,
        texture_worst=10,
        area_worst=1000,
    )

    # Send a POST request to the /predict endpoint
    response = client.post("/predict", json=data.dict())

    # Check that the response status code is 200
    assert response.status_code == 200

    # Check that the response is a JSON object
    assert isinstance(response.json(), dict)

    # Check that the response JSON object has a "prediction" key
    assert "prediction" in response.json()