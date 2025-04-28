from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class UiMovie:
    """
    Класс, содержащий методы для работы с поисковой строкой.
    """
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @allure.step("Поиск по имени персоны или названию фильма/сериала")
    def search(self, title: str):
        """
        Осуществляет поиск по введёному запросу.

        :param title: str - название фильма/сериала или имя персоны.
        """
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a[href='/s/']")
            )
        )
        self.__driver.find_element(By.CSS_SELECTOR,
                                   "input[name=kp_query]").click()
        self.__driver.find_element(By.CSS_SELECTOR,
                                   "input[name=kp_query]").send_keys(
            title, Keys.RETURN
        )

    @allure.step("Получение списка фильмов/сериалов")
    def search_film_results(self):
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.element.most_wanted")
            )
        )
        mw = self.__driver.find_element(
            By.CSS_SELECTOR, "div.element.most_wanted"
        )
        mw.find_element(By.CSS_SELECTOR, "a[data-type='film']").click()
