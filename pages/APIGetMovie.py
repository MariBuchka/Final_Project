import allure
from baseAPI import BaseAPI


class GetMovie(BaseAPI):
    """
    Класс, содержащий методы получения информации о фильмах/сериалах.
    """
    def __init__(self):
        super().__init__("/v1.4/movie/")

    @allure.step("Поиск фильма/сериала по id {movie_id}")
    def get_movie(self, movie_id: int):
        """
        Выводит всю имеющуюся информацию о фильме по ID.

        :param movie_id: int - ID фильма/сериала из Кинопоиска.
        """
        return self._get(f"{movie_id}")
