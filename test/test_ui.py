import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import main_url, cookies
from pages.UIMainPage import UiMovie
from pages.UIPersonPage import UiPerson
from pages.UITopCollection import UiTopCollection
from pages.UIAdvancedSearch import UiAdvancedSearch
from pages.UIDirectorPage import UiDirector


@pytest.fixture
def web_driver():
    chrome_options = Options()
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(web_driver):
    """
    Фикстура для авторизации пользователя (подкладываем cookies).
    """
    web_driver.get(main_url)

    for cookie in cookies:
        web_driver.add_cookie(cookie)

    web_driver.refresh()
    return web_driver


@pytest.fixture
def top_collection_page(main_page):
    return UiTopCollection(main_page)


@allure.epic("UI Testing")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Проверка работы поиска сайта Кинопоиск")
@allure.id("UI-1")
@allure.title("Поиск фильма в подборках")
def test_search_in_lists(top_collection_page: UiTopCollection):
    """
    Тест проверяет поиск фильма в подборках.

    :param collection: str - ссылка на список фильмов.
    :param number_in_list: int - номер фильма в списке.
    :param title: str - название фильма.
    """
    with allure.step("Заполнение данных для поиска"):
        collection = "/theme_school/"
        number_in_list = 1
        title = "Общество мертвых поэтов"

    with allure.step("Проверка наличия искомого фильма в списке"):
        text = top_collection_page.get_title_from_collection(
            collection, number_in_list
        )
    assert text == title


@pytest.fixture
def advanced_search_page(main_page):
    return UiAdvancedSearch(main_page)


@allure.id("UI-2")
@allure.title("Использование функции расширенного поиска фильмов "
              "по стране и жанру")
def test_advanced_search(advanced_search_page: UiAdvancedSearch):
    """
    Тест проверяет корректность работы расширенного поиска
    по таким параметрам, как 'Страна' и 'Жанр'.
    """
    with allure.step("Заполнение полей страна и жанр"):
        country = "Россия"
        genre = "комедия"

    with allure.step("Расширенный поиск фильмов по стране и жанру"):
        result = advanced_search_page.search_by_country_and_genre(
            country, genre
        )
    assert "Результаты поиска" in result


@pytest.fixture
def movie_page(main_page):
    return UiMovie(main_page)


@pytest.fixture
def person_page(main_page):
    return UiPerson(main_page)


@allure.id("UI-3")
@allure.title("Поиск конкретного фильма и актёра в главной роли")
def test_search_for_film(movie_page: UiMovie, person_page: UiPerson):
    """
    Тест проверяет поиск главного актера фильма.
    """
    with allure.step("Выбор конкретного фильма и актёра"):
        title = "Матрица"
        actor = "Киану Ривз"

    with allure.step("Поиск по названию фильма"):
        movie_page.search(title)

    with allure.step("Выбор первого фильма из полученного списка"):
        movie_page.search_film_results()

    with allure.step("Проверка актёра в главной роли"):
        result = person_page.find_main_cast()
    assert actor in result


@allure.id("UI-4")
@allure.title("Поиск фильма из списка лучших у актёра")
def test_actor_film_list(movie_page: UiMovie, person_page: UiPerson):
    """
    Тест проверяет наличие конкретного фильма
    в фильмографии актёра.
    """
    with allure.step("Выбор интересующего актёра и указание фильма, "
                     "в котором он играл"):
        name = "Нил Патрик Харис"
        title = "Как я встретил вашу маму"

    with allure.step("Запрос на поиск актёра по имени"):
        movie_page.search(name)

    with allure.step("Получение первого актёра из списка. "
                     "Переход на его страницу"):
        person_page.search_person_results()

    with allure.step("Получение списка лучших фильмов актёра"):
        films = person_page.get_top_films_by_actor()
    assert title in films


@pytest.fixture
def director_page(main_page):
    return UiDirector(main_page)


@allure.id("UI-5")
@allure.title("Поиск фильма по режиссёру")
def test_director_film_list(movie_page: UiMovie, person_page: UiPerson,
                            director_page: UiDirector):
    """
    Тест проверяет возможность поиска фильма по режиссёру.
    """
    with allure.step("Выбор конкретного режиссёра "
                     "и фильма, который он снимал"):
        name = "Леонид Гайдай"
        title = "Спортлото-82"

    with allure.step("Поиск режиссёра по имени"):
        movie_page.search(name)

    with allure.step("Переход на страницу первой в списке персоны"):
        person_page.search_person_results()

    with allure.step("Получение списка фильмов режиссёра"):
        films = director_page.get_film_list_of_director()
    assert title in films
