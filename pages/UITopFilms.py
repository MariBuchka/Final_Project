from selenium.webdriver.common.by import By
from config import Config
from pages.UIBasePage import BasePage


class TopPage(BasePage):
    TOP_LIST = (By.CSS_SELECTOR, ".styles_root__2aFPv .styles_row__3h9V0")
    TOP_250_BUTTON = (By.XPATH, "//button[contains(., 'Топ 250')]")
    YEAR_FILTER = (By.NAME, "year")

    def __init__(self, browser):
        super().__init__(browser, f"{Config.base_url}/top/")

    def get_top_movies_count(self):
        return len(self.browser.find_elements(*self.TOP_LIST))

    def open_top_250(self):
        self.element(self.TOP_250_BUTTON).click()

    def filter_by_year(self, year):
        self.element(self.YEAR_FILTER).send_keys(str(year))
