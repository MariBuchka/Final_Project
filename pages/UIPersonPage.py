from selenium.webdriver.common.by import By
from pages.UIMainPage import MainPage


class PersonPage(MainPage):
    """
    Класс для работы со страницей персоны.
    """
    PERSON_NAME = (By.CSS_SELECTOR, ".styles_name__3bk8H")
    FILMOGRAPHY_ITEMS = (By.CSS_SELECTOR, ".styles_filmography__2JvMj .styles_row__3h9V0")
    FAVORITE_BUTTON = (By.CSS_SELECTOR, "[aria-label='Добавить в любимые звезды']")

    def open(self, person_id):
        self.browser.get(f"https://www.kinopoisk.ru/name/{person_id}/")

    def get_person_name(self):
        return self._wait_for_elements(*self.PERSON_NAME).text

    def toggle_favorite(self):
        button = self._wait_for_elements(*self.FAVORITE_BUTTON)
        initial_state = button.get_attribute("aria-checked")
        button.click()
        return initial_state
