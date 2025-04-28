import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from config import main_url


class MainPage:
    """
    Класс для работы с главной страницей.

    Основные локаторы:
    SEARCH_INPUT - поисковая строка на главной странице.
    SERIES_LINK - элемент на главной странице для перехода в раздел "Сериалы".
    SIDE_MENU_FILMS - элемент на главной странице для перехода в раздел "Фильмы".
    RATING_BUTTON - элемент для активирования возможности оценки фильма.
    FAVORITE_STAR_BUTTON - элемент для добавления сохранения персоны.
    """
    SEARCH_INPUT = (By.NAME, "kp_query")
    SERIES_LINK = (By.LINK_TEXT, "Сериалы")
    SIDE_MENU_FILMS = (By.XPATH, "//a[contains(text(),'Фильмы')]")
    RATING_BUTTON = (By.CSS_SELECTOR, ".rating-button")
    FAVORITE_STAR_BUTTON = (By.CSS_SELECTOR, "[aria-label='Добавить в любимые звезды']")

    def __init__(self, browser):
        self.browser = browser
        self.url = main_url
        self.browser.get(self.url)

    @allure.step("Ожидание появления элемента(ов)")
    def _wait_for_elements(self, by, value, multiple=False, timeout=10):
        """
        Ожидает появления элемента(ов) на странице.

        :param by: str - способ поиска элемента (By.ID, By.XPATH и т.д.).
        :param value: str - значение локатора (например, "//div[@class='example']").
        :param timeout: int - максимальное время ожидания в секундах. По умолчанию 10.

        Returns:
            WebElement или List[WebElement]: Найденный элемент или список элементов.

        Raises:
            TimeoutException: Если элемент(ы) не появились в течение заданного времени.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located((by, value)))

    @allure.step("Получение заголовка страницы")
    def check_page_title(self, expected_title):
        """
        Проверяет, соответствует ли заголовок страницы ожидаемому значению.

        :param expected_title: str - ожидаемый заголовок страницы.
        """
        WebDriverWait(self.browser, 10).until(lambda b: b.title != "")
        return self.browser.title == expected_title

    @allure.step("Поиск контента по фрагменту: {query}")
    def search(self, query):
        """
        Выполняет поиск по запросу.

        :param query: str - фрагмент поискового запроса.
        """
        search_field = self._wait_for_elements(*self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(query + Keys.RETURN)

    @allure.step("Переход в раздел 'Сериалы'")
    def navigate_to_series(self):
        """
        Переходит в раздел сериалов.
        """
        self._wait_for_elements(*self.SERIES_LINK).click()
        return self.browser.current_url
