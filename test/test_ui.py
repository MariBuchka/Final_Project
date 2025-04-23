import allure
import pytest
from selenium import webdriver
from pages.UIMainPage import MainPage
from pages.UISearchPage import SearchPage
from pages.UIMoviePage import MoviePage
from pages.UISeriesPage import SeriesPage


@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

@allure.feature("UI Тесты Кинопоиска")
class TestKinopoiskUI:
    @allure.story("Поиск")
    @allure.title("Поиск существующего фильма")
    def test_search_existing_movie(self, browser):
        """
        Тест проверяет функционал поиска фильмов по названию.
        """
        main_page = MainPage(browser)
        search_page = SearchPage(browser)

        with allure.step("1. Открыть главную страницу"):
            main_page.open_kinopoisk()

        with allure.step("2. Выполнить поиск фильма 'Матрица'"):
            main_page.search("Матрица")

        with allure.step("3. Проверить результаты поиска"):
            assert "Матрица" in search_page.get_first_result_text(), "Фильм не найден"
            assert search_page.get_results_count() > 0, "Нет результатов поиска"

    @allure.story("Навигация")
    @allure.title("Проверка работы главного меню")
    def test_main_navigation(self, browser):
        """
        Тест проверяет навигацию по основным разделам сайта
        """
        main_page = MainPage(browser)
        series_page = SeriesPage(browser)

        with allure.step("1. Открыть главную страницу"):
            main_page.open_kinopoisk()

        with allure.step("2. Проверить пункты меню"):
            menu_items = main_page.get_menu_items()
            expected_items = ["Фильмы", "Сериалы", "Мультфильмы"]
            for item in expected_items:
                assert item in menu_items, f"Раздел '{item}' отсутствует"

        with allure.step("3. Перейти в раздел 'Сериалы'"):
            main_page.series_link.click()
            assert series_page.get_series_count() > 0, "Нет списка сериалов"

    @allure.story("Фильтры поиска")
    @allure.title("Применение фильтров по году выпуска")
    def test_search_filters(self, browser):
        """
        Тест проверяет работу фильтров при поиске
        """
        search_page = SearchPage(browser)

        with allure.step("1. Открыть расширенный поиск"):
            search_page.open_advanced_search()

        with allure.step("2. Установить фильтр по годам"):
            search_page.apply_year_filter(2020, 2023)

        with allure.step("3. Проверить результаты фильтрации"):
            assert search_page.get_results_count() > 0, "Нет результатов после фильтрации"

    @allure.story("Информация о фильме")
    @allure.title("Проверка отображения информации о фильме")
    def test_movie_info(self, browser):
        """
        Тест проверяет корректность отображения информации о фильме
        """
        movie_page = MoviePage(browser)

        with allure.step("1. Открыть страницу фильма"):
            movie_page.open(435)  # ID "Зеленая миля"

        with allure.step("2. Проверить основные данные"):
            assert movie_page.get_movie_title() == "Зеленая миля"
            assert movie_page.get_movie_year() == 1999
            assert movie_page.get_movie_rating() >= 8.0

    @allure.story("Сериалы")
    @allure.title("Проверка навигации по сезонам")
    def test_series_seasons(self, browser):
        """
        Тест проверяет переключение между сезонами сериалов
        """
        series_page = SeriesPage(browser)

        with allure.step("1. Открыть страницу сериалов"):
            series_page.open_series()

        with allure.step("2. Открыть первый сериал из списка"):
            series_page.open_series(0)

        with allure.step("3. Выбрать 1 сезон"):
            series_page.select_season(1)
            assert series_page.get_episodes_count() > 0, "Нет списка серий"
