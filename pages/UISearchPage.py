from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config import Config
from pages.UIBasePage import BasePage


class SearchPage(BasePage):
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".search_results .item")
    FIRST_RESULT = (By.CSS_SELECTOR, ".search_results .item:first-child")
    ADVANCED_SEARCH_BTN = (By.CSS_SELECTOR, ".styles_advanced__1vbqM")
    YEAR_FILTER = (By.NAME, "year")
    RATING_FILTER = (By.NAME, "rating")

    def get_results_count(self):
        return len(self.browser.find_elements(*self.SEARCH_RESULTS))

    def get_first_result_text(self):
        return self.element(self.FIRST_RESULT).text

    def open_advanced_search(self):
        self.element(self.ADVANCED_SEARCH_BTN).click()

    def apply_year_filter(self, year_from, year_to):
        year_field = self.element(self.YEAR_FILTER)
        year_field.clear()
        year_field.send_keys(f"{year_from}-{year_to}")
        year_field.send_keys(Keys.RETURN)

    def apply_rating_filter(self, min_rating):
        self.element(self.RATING_FILTER).send_keys(str(min_rating))
