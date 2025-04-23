import allure
from baseAPI import BaseAPI


class SearchMovies(BaseAPI):

    def __init__(self):
        super().__init__("/v1.4/movie/search")

    @allure.step("Поиск фильма/сериала по названию {query}")
    def search_movies(self, query: str, page: int = 1, limit: int = 10):
        """
        Осуществляет поиск фильмов/сериалов по названию.

        :param query: str - название фильма/сериала.
        :param page: int - страница выборки.
        :param limit: int - количество элементов на странице.
        """
        return self._get(params={"query": query, "page": page, "limit": limit})
