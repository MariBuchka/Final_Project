import allure
import pytest

from pages.APIGetMovie import GetMovie
from pages.APIGetPerson import GetPerson
from pages.APISearchMovies import SearchMovies
from pages.APISearchPersons import SearchPersons


@allure.epic("API Testing")
@allure.severity(allure.severity_level.CRITICAL)
class TestKinopoiskAPI:
    """
    Фикстуры для инициализации методов классов:
        GetMovie - для получения всей информации о конкретном фильме по его id.
        GetPerson - для получения всей информации о конкретной персоне по id.
        SearchMovies - для поиска фильмов по названию.
        SearchPersons - для поиска персон по имени.
    """
    @pytest.fixture
    def movie_api(self):
        return GetMovie()

    @pytest.fixture
    def person_api(self):
        return GetPerson()

    @pytest.fixture
    def search_movies_api(self):
        return SearchMovies()

    @pytest.fixture
    def search_persons_api(self):
        return SearchPersons()

    # Позитивные тесты
    @allure.feature("Positive Tests")
    @allure.story("Поиск существующих фильмов/сериалов")
    @allure.title("Поиск фильма/сериала по названию ")
    @pytest.mark.parametrize(
        "query, expected",
        [
            ("Такси", "Такси"),
            ("Matrix", "Матрица"),
            ("Криминальное чтиво", "Криминальное чтиво"),
            ("HarryPotter", "Гарри Поттер"),
            ("Garfield: the movie", "Гарфилд"),
            ("100 дней после детства", "100 дней"),
        ],
    )
    def test_search_movies_positive(self, search_movies_api, query, expected):
        """
        Тест проверяет корректность поиска фильмов/сериалов по названию.

        :param search_movies_api: экз-р класса SearchMovies, предоставляющий
                                    методы для работы с API поиска фильмов.
        :param query: str - название фильма/сериала для поиска.
        :param expected: str - ожидаемый фрагмент названия
                                    в результатах поиска.
        """
        with allure.step(f"Поиск фильма/сериала по названию '{query}'"):
            result = search_movies_api.search_movies(query)

        with allure.step("Проверка результатов"):
            assert result["total"] > 0
            assert any(expected in movie["name"] for movie in result["docs"])

    @allure.feature("Positive Tests")
    @allure.story("Поиск существующих фильмов/сериалов")
    @allure.title("Поиск фильма/сериала по id")
    @pytest.mark.parametrize(
        "movie_id, expected",
        [
            (435, "Зеленая миля"),
            (328, "Властелин колец: Братство кольца"),
            (666, "Форсаж"),
            (401522, "Как я встретил вашу маму")
        ],
    )
    def test_get_movie_by_id_positive(self, movie_api, movie_id, expected):
        """
        Тест проверяет корректность поиска фильмов/сериалов по id.

        :param movie_api: экз-р класса GetMovie, предоставляющий
                                    методы для работы с API поиска фильмов.
        :param movie_id: int - ID фильма/сериала из Кинопоиска.
        :param expected: str - ожидаемый фрагмент названия фильма
                                    в результатах поиска.
        """
        with allure.step(f"Поиск фильма/сериала по id {movie_id}"):
            result = movie_api.get_movie(movie_id)

        with allure.step("Проверка данных фильма"):
            assert result["name"] == expected
            assert result["id"] == movie_id

    @allure.feature("Positive Tests")
    @allure.story("Поиск существующей персоны")
    @allure.title("Поиск персоны по имени")
    @pytest.mark.parametrize(
        "query, expected",
        [
            ("Леонардо ДиКаприо", "ДиКаприо"),
            ("Булгаков", "Булгаков"),
            ("Панкратов-Черный Александр", "Панкратов-Чёрный"),
            ("UMA KARUNA THURMAN", "Ума Карина"),
        ],
    )
    def test_search_person_positive(self, search_persons_api, query, expected):
        """
        Тест проверяет корректность поиска персон
        (актеров, режиссеров и т.д.) по именам.

        :param search_persons_api: экз-р класса SearchPersons, предоставляющий
                                    методы для работы с API поиска персон.
        :param query: str - имя персоны (актера, режиссера и т.д.).
        :param expected: str - ожидаемый фрагмент имени
                                    в результатах поиска.
        """
        with allure.step(f"Поиск персоны по запросу '{query}'"):
            result = search_persons_api.search_persons(query)

        with allure.step("Проверка результатов"):
            assert result["total"] > 0
            assert any(expected in person["name"] for person in result["docs"])

    @allure.feature("Positive Tests")
    @allure.story("Поиск существующей персоны")
    @allure.title("Поиск персоны по id")
    @pytest.mark.parametrize(
        "person_id, expected",
        [
            (30875, "Орландо Блум"),
            (257004, "Александр Панкратов-Чёрный"),
        ],
    )
    def test_get_person_by_id_positive(self, person_api, person_id, expected):
        """
        Тест проверяет корректность поиска персоны по id.

        :param person_api: экз-р класса GetPerson, предоставляющий
                                    методы для работы с API поиска персон.
        :param person_id: int - ID персоны из Кинопоиска.
        :param expected: str - ожидаемый фрагмент имени персоны
                                    в результатах поиска.
        """
        with allure.step(f"Поиск персоны по id {person_id}"):
            result = person_api.get_person(person_id)

        with allure.step("Проверка данных персоны"):
            assert result["name"] == expected
            assert result["id"] == person_id

    # Негативные тесты
    @allure.feature("Negative Tests")
    @allure.story("Поиск несуществующего фильма")
    @allure.title("Поиск по некорректному названию")
    @pytest.mark.parametrize(
        "query",
        [
            "Несущприфе-maje-3",
            "%Mos$co'",
        ],
    )
    def test_search_nonexistent_movie(self, search_movies_api, query):
        """
        Тест проверяет корректность обработки системой запросов
        с несуществующими названиями фильмов.

        :param search_movies_api: экз-р класса SearchMovies, предоставляющий
                                    методы для работы с API поиска фильмов.
        :param query: str - невалидное название фильма.
        """
        with allure.step(f"Поиск несуществующего фильма по запросу '{query}'"):
            result = search_movies_api.search_movies(query)

        with allure.step("Проверка результатов"):
            assert result["total"] == 0
            assert len(result["docs"]) == 0

    @allure.feature("Negative Tests")
    @allure.story("Поиск несуществующего фильма")
    @allure.title("Поиск по невалидному id")
    @pytest.mark.parametrize(
        "invalid_id",
        [
            -1,
            999999999,
        ],
    )
    def test_get_movie_by_invalid_id(self, movie_api, invalid_id):
        """
        Тест проверяет корректность обработки системой запросов
        с невалидным значением id фильма/сериала.

        :param movie_api: экз-р класса GetMovie, предоставляющий
                                    методы для работы с API поиска фильмов.
        :param invalid_id: int - невалидное значение ID фильма/сериала.
        """
        with allure.step(f"Получение фильма с неверным ID {invalid_id}"):
            try:
                movie_api.get_movie(invalid_id)
                assert False, 'Запрос должен был вернуть ошибку 400'
            except Exception as e:
                assert "400" in str(e), (f"Ожидалась ошибка 400, "
                                         f"получено: {str(e)}")

    @allure.feature("Negative Tests")
    @allure.story("Поиск несуществующего фильма")
    @allure.title("Пустой запрос")
    def test_search_movie_empty_query(self, search_movies_api):
        """
        Тест проверяет корректность обработки системой
        пустого запроса на поиск фильма.

        :param search_movies_api: экз-р класса SearchMovies, предоставляющий
                                    методы для работы с API поиска фильмов.
        """
        with allure.step("Отправка пустого запроса"):
            result = search_movies_api.search_movies("")

        with allure.step("Проверка результатов"):
            assert result["total"] > 0

    @allure.feature("Negative Tests")
    @allure.story("Поиск несуществующей персоны")
    @allure.title("Поиск по некорректному имени")
    @pytest.mark.parametrize(
        "query",
        [
            "Мишка-косолапый",
            "Nonexistent Person 123",
        ],
    )
    def test_search_nonexistent_person(self, search_persons_api, query):
        """
        Тест проверяет корректность обработки системой запросов
        на поиск несуществующих персон.

        :param search_persons_api: экз-р класса Searchersons, предоставляющий
                                    методы для работы с API поиска персон.
        :param query: str - невалидное имя персонажа.
        """
        with allure.step(f"Поиск несуществующей персоны по запросу '{query}'"):
            result = search_persons_api.search_persons(query)

        with allure.step("Проверка результатов"):
            assert result["total"] == 0 or all(
                query not in person["name"] for person in result["docs"]
            )

    @allure.feature("Negative Tests")
    @allure.story("Поиск несуществующей персоны")
    @allure.title("Поиск по невалидному id")
    @pytest.mark.parametrize(
        "invalid_id",
        [
            -1,
            30000001,
        ],
    )
    def test_get_person_by_invalid_id(self, person_api, invalid_id):
        """
        Тест проверяет корректность обработки системой запросов
        с невалидным значением id персоны.

        :param person_api: экз-р класса GetPerson, предоставляющий
                            методы для работы с API поиска персон.
        :param invalid_id: int - невалидное значение ID персоны.
        """
        with allure.step(f"Получение персоны с неверным ID {invalid_id}"):
            try:
                person_api.get_person(invalid_id)
                assert False, "Запрос должен был вернуть ошибку 400"
            except Exception as e:
                assert "400" in str(e), (f"Ожидалась ошибка 400, "
                                         f"получено: {str(e)}")
