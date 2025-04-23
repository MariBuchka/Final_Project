from selenium.webdriver.common.by import By
from config import Config
from pages.UIBasePage import BasePage


class SeriesPage(BasePage):
    SERIES_LIST = (By.CSS_SELECTOR, ".styles_root__1h4WF .styles_item__3ffNr")
    SEASON_SELECTOR = (By.CSS_SELECTOR, ".styles_seasons__2q1C4")
    EPISODE_LIST = (By.CSS_SELECTOR, ".styles_episodes__3zGXH")

    def __init__(self, browser):
        super().__init__(browser, f"{Config.base_url}/series/")

    def get_series_count(self):
        return len(self.browser.find_elements(*self.SERIES_LIST))

    def open_series(self, index=0):
        self.browser.find_elements(*self.SERIES_LIST)[index].click()

    def select_season(self, season_num):
        seasons = self.element(self.SEASON_SELECTOR)
        seasons.find_element(By.XPATH, f"//option[contains(., '{season_num}')]").click()

    def get_episodes_count(self):
        return len(self.browser.find_elements(*self.EPISODE_LIST))
