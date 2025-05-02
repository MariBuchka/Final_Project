import allure
from baseAPI import BaseAPI


class SearchPersons(BaseAPI):
    """
    Класс, содержащий методы поиска персон.
    """
    def __init__(self):
        super().__init__("/v1.4/person/search")

    @allure.step("Поиск персоны по запросу {query}")
    def search_persons(self, query: str, page: int = 1, limit: int = 10):
        """
        Осуществляет поиск персон (актеров, режиссеров и т.д.) по именам.

        :param query: str - имя персоны (актера, режиссера и т.д.).
        :param page: int - страница выборки.
        :param limit: int - количество элементов на странице.
        """
        return self._get(params={"query": query, "page": page, "limit": limit})
