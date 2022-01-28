from locust import HttpUser, task
from http import HTTPStatus

class SearchQuery(HttpUser):    
    @task
    def search(self):
        url = "data/2.5/find"

        querystring = {"q": "hanoi", "appid": "439d4b804bc8187953eb36d2a8c26a02"}

        headers = {
            "Host": "openweathermap.org",
            "Referer": "https://openweathermap.org/",
        }

        with self.client.get(
            url,
            headers=headers,
            params=querystring,
            catch_response=True,
        ) as response:
            if response.status_code == HTTPStatus.OK:
                response.success()
            else:
                response.failure(f"Failed! Http Code `{response.status_code}`")

