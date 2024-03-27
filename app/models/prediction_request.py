from pydantic import BaseModel

class PredictionRequest(BaseModel):
    concavity_mean: float
    concave_points_mean: float
    perimeter_se: float
    area_se: float
    texture_worst: float
    area_worst: float