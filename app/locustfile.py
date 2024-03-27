from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)
    verify = False  # Disable SSL verification
    @task
    def predict(self):
        self.client.post("/predict", json={
            "concavity_mean": 0.1,
            "concave_points_mean": 0.05,
            "perimeter_se": 75,
            "area_se": 500,
            "texture_worst": 10,
            "area_worst": 1000,
        })