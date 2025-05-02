from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class UiPerson:
    """
    Класс, содержащий методы для поиска персон
    и вывода информации о них.
    """
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @allure.step("Получение имен главных актёров")
    def find_main_cast(self):
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.dub.dub1.dub_first")
            )
        )
        actor = self.__driver.find_element(
            By.CSS_SELECTOR, "div.dub.dub1.dub_first"
        )
        actor_name = actor.find_element(By.CSS_SELECTOR, "div.name")
        return actor_name.text

    @allure.step("Получение первого актёра из списка. "
                 "Переход на его страницу")
    def search_person_results(self):
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.element.most_wanted")
            )
        )
        mw = self.__driver.find_element(
            By.CSS_SELECTOR, "div.element.most_wanted"
        )
        name = mw.find_element(By.CSS_SELECTOR, "p.name")
        name.find_element(By.CSS_SELECTOR, "a[data-type='person']").click()

    @allure.step("Получение списка лучших фильмов актёра")
    def get_top_films_by_actor(self):
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.styles_bestMovies__P4zSv")
            )
        )
        film_list = self.__driver.find_elements(
            By.CSS_SELECTOR, "a.styles_link__Act80"
        )
        list_of_films = [film.text for film in film_list]
        return list_of_films
