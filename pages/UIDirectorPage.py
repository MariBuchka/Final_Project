from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class UiDirector:
    """
    Класс, содержащий методы для получения списка
    фильмов конкретного режиссёра.
    """
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @allure.step("Получение списка фильмов режиссёра")
    def get_film_list_of_director(self):
        """
        Выводит список всех фильмов конкретного режиссёра.
        """
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.styles_bestMovies__P4zSv")
            )
        )
        self.__driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        film_list = self.__driver.find_elements(
            By.CSS_SELECTOR, "span[data-tid='4502216a']"
        )
        list_of_films = [film.text for film in film_list]
        return list_of_films
