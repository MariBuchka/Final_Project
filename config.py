class Config:
    base_url = "https://www.kinopoisk.ru"
    api_base_url = "https://api.kinopoisk.dev"
    api_token = "TE38DPK-58B48CX-QEAEHF5-6ANK8VP"

    def __init__(self):
        self.headers = {
            "X-API-KEY": self.api_token,
            "Content-Type": "application/json"
        }
