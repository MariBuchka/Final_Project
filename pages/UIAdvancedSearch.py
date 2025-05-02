from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import allure


class UiAdvancedSearch:
    """
    Класс, содержащий методы для работы
    с расширенным поиском.
    """
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @allure.step("Расширенный поиск фильмов по стране и жанру")
    def search_by_country_and_genre(self, country: str, genre: str):
        """
        Выводит список фильмов, удовлетворяющих параметрам запроса.

        :param country: str - название страны.
        :param genre: str - название жанра.
        """
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a[href='/s/']")
            )
        )
        self.__driver.find_element(By.CSS_SELECTOR, "a[href='/s/']").click()
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div#searchAdv")
            )
        )
        select_country = self.__driver.find_element(By.CSS_SELECTOR,
                                                    "select#country")
        select = Select(select_country)
        select.select_by_visible_text(country)
        select_genre = self.__driver.find_element(
            By.CSS_SELECTOR, "select.text.el_6.__genreSB__"
        )
        select = Select(select_genre)
        select.select_by_visible_text(genre)
        self.__driver.find_element(By.CSS_SELECTOR,
                                   "#formSearchMain > "
                                   "input.el_18.submit.nice_button").click()
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.search_results")
            )
        )
        results = self.__driver.find_element(
            By.CSS_SELECTOR, "div.search_results.search_results_last"
        )
        return results.text
