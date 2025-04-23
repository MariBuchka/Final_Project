from selenium.webdriver.common.by import By
from config import Config
from pages.UIBasePage import BasePage


class MoviePage(BasePage):
    MOVIE_TITLE = (By.CSS_SELECTOR, ".styles_title__3kbkm h1")
    MOVIE_YEAR = (By.CSS_SELECTOR, ".styles_year__2GXQR")
    MOVIE_RATING = (By.CSS_SELECTOR, ".styles_rating__2XaDp")
    RATE_BUTTON = (By.CSS_SELECTOR, ".styles_ratingBtn__1XHNR")
    RATING_STARS = (By.CSS_SELECTOR, ".styles_ratingStars__3zP5Z span")
    CURRENT_RATING = (By.CSS_SELECTOR, ".styles_userRating__1Xlkr")

    def open(self, movie_id):
        self.browser.get(f"{Config.base_url}/film/{movie_id}/")

    def get_movie_title(self):
        return self.element(self.MOVIE_TITLE).text

    def get_movie_year(self):
        return int(self.element(self.MOVIE_YEAR).text)

    def get_movie_rating(self):
        return float(self.element(self.MOVIE_RATING).text)

    def rate_movie(self, stars):
        self.element(self.RATE_BUTTON).click()
        stars_element = self.browser.find_elements(*self.RATING_STARS)[stars - 1]
        stars_element.click()

    def get_current_rating(self):
        return self.element(self.CURRENT_RATING).text
