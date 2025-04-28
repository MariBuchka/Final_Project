import allure
from selenium.webdriver.common.by import By
from pages.UIMainPage import MainPage


class SeriesPage(MainPage):
    """
    Класс страницы сериалов.

    Локатор
    SERIES_LIST -
    """
    SERIES_LIST = (By.CSS_SELECTOR, ".styles_root__1h4WF .styles_item__3ffNr")
    SEASON_SELECTOR = (By.CSS_SELECTOR, ".season-selector")

    @allure.step("")
    def get_series_count(self):
        return len(self._wait_for_elements(*self.SERIES_LIST, multiple=True))

    def select_season(self, season_num):
        """Выбрать сезон сериала (п.8)."""
        selector = self._wait_for_elements(*self.SEASON_SELECTOR)
        selector.click()
        season_option = self._wait_for_elements(By.XPATH, f"//option[contains(text(),'Сезон {season_num}')]")
        season_option.click()
