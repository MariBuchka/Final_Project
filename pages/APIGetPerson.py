import allure
from baseAPI import BaseAPI


class GetPerson(BaseAPI):
    """
    Класс, содержащий методы получения информации о персонах.
    """
    def __init__(self):
        super().__init__("/v1.4/person/")

    @allure.step("Поиск персоны по id {person_id}")
    def get_person(self, person_id: int):
        """
        Выводит всю имеющуюся информацию о персоне по ID.

        :param person_id: int - ID персоны из Кинопоиска.
        """
        return self._get(f"{person_id}")
