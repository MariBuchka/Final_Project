import requests
from config import APIConfig


class BaseAPI(APIConfig):
    def __init__(self, endpoint=""):
        super().__init__()
        self.base_url = f"{self.api_base_url}{endpoint}"

    def _get(self, path="", params=None):
        url = f"{self.base_url}{path}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
