main_url = 'https://www.kinopoisk.ru/'
cookie_string = ''
def parse_cookies(cookie_string):
    cookies = []
    for cookie in cookie_string.split(';'):
        name, value = cookie.strip().split('=', 1)
        cookies.append({'name': name, 'value': value, 'path': '/'})
    return cookies

cookies = parse_cookies(cookie_string)

class APIConfig:
    api_base_url = "https://api.kinopoisk.dev"
    api_token = ""

    def __init__(self):
        self.headers = {
            "X-API-KEY": self.api_token,
            "Content-Type": "application/json"
        }
