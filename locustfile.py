from locust import HttpUser, task, between


class BentoMLUser(HttpUser):
    wait_time = between(1, 3)  # Wait 1-3 seconds between tasks

    @task
    def predict(self):
        # Adjust the endpoint and payload according to your BentoML model
        self.client.post("/summarize")

    @task
    def healthcheck(self):
        self.client.get("/healthz")
