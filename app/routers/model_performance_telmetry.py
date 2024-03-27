from prometheus_client import generate_latest, REGISTRY, Gauge
from fastapi import APIRouter

router = APIRouter()

# Create a Gauge metric for accuracy prediction
accuracy_gauge = Gauge('model_accuracy', 'Accuracy of model prediction', registry=REGISTRY)


@router.get("/health")
def read_health():
    # Read accuracy from file
    accuracy_file = "./data/accuracy.txt"
    with open(accuracy_file, 'r') as f:
        accuracy = float(f.read().strip())

    # Set the accuracy gauge to the read accuracy
    accuracy_gauge.set(accuracy)

    # Generate the latest metrics in the Prometheus exposition format
    metrics_page = generate_latest(REGISTRY)
    return metrics_page
