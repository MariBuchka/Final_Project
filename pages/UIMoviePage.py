from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.UIMainPage import MainPage


class MoviePage(MainPage):
    """
    Класс страницы фильма.

    Локаторы:
    MOVIE_TITLE
    MOVIE_YEAR
    MOVIE_RATING
    USER_RATING - оценка пользователя.
    STAR_RATING - локатор звезды.
    """
    MOVIE_TITLE = (By.CSS_SELECTOR, ".styles_title__3kbkm h1")
    MOVIE_YEAR = (By.CSS_SELECTOR, ".styles_year__2GXQR")
    MOVIE_RATING = (By.CSS_SELECTOR, ".styles_rating__2XaDp")
    USER_RATING = (By.CSS_SELECTOR, ".user-rating")
    STAR_RATING = (By.XPATH, "//div[@class='star'][8]")


    def open(self, movie_id):
        """Открывает страницу фильма по ID."""
        self.browser.get(f"{self.url}film/{movie_id}/")

    def get_movie_title(self):
        return self._wait_for_elements(*self.MOVIE_TITLE).text

    def get_movie_year(self):
        return int(self._wait_for_elements(*self.MOVIE_YEAR).text)

    def get_movie_rating(self):
        return float(self._wait_for_elements(*self.MOVIE_RATING).text)

    def rate_movie(self, score):
        """Поставить оценку фильму (п.5)."""
        self._wait_for_elements(*self.RATING_BUTTON).click()
        star = self._wait_for_elements(By.XPATH, f"//div[@class='star'][{score}]")
        ActionChains(self.browser).move_to_element(star).click().perform()

    def get_user_rating(self):
        """Получить текущую оценку пользователя."""
        return self._wait_for_elements(*self.USER_RATING).text
