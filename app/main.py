import time

from prometheus_client import Summary

from app.routers import predict
from fastapi import FastAPI, Request
from app.routers import model_performance_telmetry

app = FastAPI()
# Create a Summary object to track execution time of your model's prediction method
MODEL_PREDICTION_TIME = Summary('model_prediction_time', 'Time spent processing model prediction')
app.include_router(predict.router)
app.include_router(model_performance_telmetry.router)


@app.middleware("http")
async def monitor_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()

    # Update the Summary object
    MODEL_PREDICTION_TIME.observe(end_time - start_time)

    return response
