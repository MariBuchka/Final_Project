from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import Config
from pages.UIBasePage import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.NAME, "kp_query")
    TOP_MENU = (By.CSS_SELECTOR, ".styles_primary__3C2sK")
    SERIES_LINK = (By.LINK_TEXT, "Сериалы")
    MOVIES_LINK = (By.LINK_TEXT, "Фильмы")

    def __init__(self, browser):
        super().__init__(browser, f"{Config.base_url}")

    def search(self, query):
        self.element(self.SEARCH_INPUT).send_keys(query)
        self.element(self.SEARCH_INPUT).send_keys(Keys.RETURN)

    def get_menu_items(self):
        return [item.text for item in self.browser.find_elements(*self.TOP_MENU)]


    @property
    def series_link(self):
        return self.element(self.SERIES_LINK)

    def navigate_to_series(self):
        self.series_link.click()
