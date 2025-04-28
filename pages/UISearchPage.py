from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import re


class SearchPage:
    """
    Класс страницы результатов поиска.
    """
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".search-results__item")  # Уточненный локатор
    NO_RESULTS_MSG = (By.CLASS_NAME, "search-results__empty")  # Локатор сообщения "Ничего не найдено"
    ADVANCED_SEARCH_BUTTON = (By.LINK_TEXT, "Расширенный поиск")  # Для п.7
    GENRE_CHECKBOX = (By.XPATH, "//span[contains(text(),'комедия')]/input")  # Пример для п.7
    YEAR_FROM = (By.NAME, "yearFrom")  # Для фильтра по году
    YEAR_TO = (By.NAME, "yearTo")

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Ожидание появления элемента(ов)")
    def _wait_for_elements(self, by, value, multiple=False, timeout=10):
        """
        Ожидает появления элемента(ов) на странице.

        :param by: str - способ поиска элемента (By.ID, By.XPATH и т.д.).
        :param value: str - значение локатора (например, "//div[@class='example']").
        :param multiple: bool - если True, ожидает список элементов, иначе — один элемент. По умолчанию False.
        :param timeout: int - максимальное время ожидания в секундах. По умолчанию 10.

        Returns:
            WebElement или List[WebElement]: Найденный элемент или список элементов.

        Raises:
            TimeoutException: Если элемент(ы) не появились в течение заданного времени.
        """
        if multiple:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located((by, value)))
        else:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((by, value)))

    def _get_element_texts(self, css_selector):
        elements = self._wait_for_elements(By.CSS_SELECTOR, css_selector, multiple=True)
        return [element.text for element in elements]

    @allure.step("Получаем названия фильмов/сериалов")
    def find_content_titles(self):
        try:
            return self._get_element_texts("[data-type='film'], [data-type='series'], [data-type='person']")
        except TimeoutException:
            return []

    @allure.step("Получаем количество результатов поиска")
    def get_search_results_count(self):
        try:
            results_text = self._wait_for_elements(By.CSS_SELECTOR, ".search_results_topText").text

            match = re.search(r'результаты:\s*(\d+)', results_text)
            return int(match.group(1)) if match else 0
        except TimeoutException:
            return 0

    def open_advanced_search(self):
        """Открыть расширенный поиск (п.7)."""
        self._wait_for_elements(*self.ADVANCED_SEARCH_BUTTON).click()

    def apply_genre_filter(self, genre):
        """Выбрать жанр в фильтрах."""
        checkbox = self._wait_for_elements(By.XPATH, f"//span[contains(text(),'{genre}')]/input")
        checkbox.click()

    def apply_year_filter(self, year_from, year_to):
        """Установить диапазон годов (п.7)."""
        self._wait_for_elements(*self.YEAR_FROM).send_keys(year_from)
        self._wait_for_elements(*self.YEAR_TO).send_keys(year_to)
