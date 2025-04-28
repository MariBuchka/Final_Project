from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class UiTopCollection:
    """
    Класс, содержащий методы для работы со списками фильмов.
    """

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__driver.get(
            "https://www.kinopoisk.ru/lists/categories/movies/1/"
        )

    @allure.step("Проверка наличия искомого фильма в списке")
    def get_title_from_collection(self, collection: str, num: int):
        """
        Возвращает название фильма,
        соответствующее указанному номеру в списке.

        :param collection:  str - ссылка на список фильмов.
        :param num: int - номер фильма в списке.
        """
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f"a[href='/lists/movies{collection}']"))
        )
        self.__driver.find_element(By.CSS_SELECTOR, f"a[href='/lists/movies"
                                                    f"{collection}']").click()
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "h1.styles_title__jB8AZ")
            )
        )
        title = self.__driver.find_elements(
            By.CSS_SELECTOR, "span[data-tid='4502216a']"
        )
        return title[num].text
