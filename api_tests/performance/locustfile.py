import os
from auth import Auth
from locust import HttpUser, task, between


class ReasonableAdjustmentsUser(HttpUser):
    wait_time = between(5, 9)

    def auth(self):
        return Auth(
            os.environ["LOCUST_HOST"],
            os.environ["CALLBACK_URL"],
            os.environ["CLIENT_ID"],
            os.environ["CLIENT_SECRET"]
        )

    def on_start(self):
        self.base_path = os.environ["BASE_PATH"]
        authenticator = self.auth()
        self.credentials = authenticator.login()
        self.headers = {
            "Authorization": self.credentials["token_type"] + " " + self.credentials["access_token"],
            "X-Request-ID": "test",
            "NHSD-Session-URID": "test",
        }

    @task(1)
    def reasonable_adjustments_api(self):
        self.client.get(f"{self.base_path}/flag?patient=9999999998&status=active&category=test", headers=self.headers)