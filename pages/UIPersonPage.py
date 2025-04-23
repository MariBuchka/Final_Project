from selenium.webdriver.common.by import By
from config import Config
from pages.UIBasePage import BasePage


class PersonPage(BasePage):
    PERSON_NAME = (By.CSS_SELECTOR, ".styles_name__3bk8H")
    FILMOGRAPHY = (By.CSS_SELECTOR, ".styles_filmography__2JvMj")
    FILMOGRAPHY_ITEMS = (By.CSS_SELECTOR, ".styles_filmography__2JvMj .styles_row__3h9V0")

    def open(self, person_id):
        self.browser.get(f"{Config.base_url}/name/{person_id}/")

    def get_person_name(self):
        return self.element(self.PERSON_NAME).text

    def get_filmography_count(self):
        return len(self.browser.find_elements(*self.FILMOGRAPHY_ITEMS))

    def get_filmography_years(self):
        return [int(item.text.split()[-1].strip('()'))
                for item in self.browser.find_elements(*self.FILMOGRAPHY_ITEMS)]
