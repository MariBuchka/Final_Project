from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url=""):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, 20)

    def open_kinopoisk(self):
        self.browser.get(self.url)

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
