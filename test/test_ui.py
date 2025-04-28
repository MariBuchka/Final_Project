import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from config import main_url, cookies
from pages.UIMainPage import MainPage
from pages.UISearchPage import SearchPage
from pages.UIMoviePage import MoviePage
from pages.UISeriesPage import SeriesPage
from pages.UIPersonPage import PersonPage


@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера (browser).
    """
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    )
    #chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def main_page(browser):
    """
    Фикстура для авторизации пользователя (подкладываем cookies).
    """
    browser.get(main_url)

    for cookie in cookies:
        browser.add_cookie(cookie)

    browser.get(main_url)
    return MainPage(browser)

@allure.feature("UI Тесты Кинопоиска")
@allure.story("Smoke")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Заголовок главной страницы"):
        assert main_page.check_page_title(
            "Кинопоиск. Онлайн кинотеатр. Фильмы сериалы мультфильмы и энциклопедия"
        )

@allure.story("Навигация")
@allure.title("Переход в раздел 'Сериалы' через боковое меню")
def test_side_menu_navigation(main_page):
    """Тест навигации через боковое меню."""
    excpected_url = "https://www.kinopoisk.ru/lists/categories/movies/3/"

    with allure.step("Найти и кликнуть на раздел 'Сериалы' в боковом меню"):
        current_url = main_page.navigate_to_series()

    with allure.step("Проверить URL страницы"):
        assert current_url == excpected_url

@allure.story("Поиск")
@allure.title("Поиск существующего фильма/сериала/персоны")
@pytest.mark.positive
@pytest.mark.parametrize(
    "query",
    [
        "ОДИН ДОМА", "Приключения Паддингтона 2", "Как Я Встретил Вашу Маму", "Нил Патрик Харрис"
    ],
)
def test_search_by_title(main_page, query):
    with allure.step(f"Поиск фильмов/сериалов/персон "
                     f"по названию/имени '{query}'"):
        main_page.search(query)

    search_page = SearchPage(main_page.browser)

    with allure.step("Проверяем, что количество результатов больше 0"):
        assert search_page.get_search_results_count() > 0

    with allure.step(f"Проверяем, что запрос '{query}'"
                     f" содержится в результатах"):
        titles = search_page.find_content_titles()
        assert any(query.lower() in title.lower() for title in titles), \
            (f"Запрос '{query}' не найден. "
            f"Результаты: {titles}")

# Тест 3: Открытие страницы через поисковые подсказки
@allure.story("Поиск")
@allure.title("Открытие страницы фильма через поисковые подсказки")
@pytest.mark.parametrize(
    "query, expected_title",
    [
        ("Зеленая миля", "Зеленая миля"),
        ("Форрест Гамп", "Форрест Гамп"),
    ],
)
def test_open_from_suggestions(main_page, query, expected_title):
    """
    Тест открытия страницы фильма через поисковые подсказки.
    """
    with allure.step(f"Ввести запрос '{query}' в поиск"):
        search_field = main_page._wait_for_elements(*MainPage.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(query)

    with allure.step("Ожидаем появления окна с подсказками"):
        main_page._wait_for_elements(By.CSS_SELECTOR, ".styles_root__oGRI_.styles_group__1mMFN.kinopoisk-header-suggest-group")

    with allure.step("Выбрать первый вариант из подсказок"):
        suggestions = main_page.browser.find_elements(By.CSS_SELECTOR, "#suggest-container .suggest-item")
        if not suggestions:
            pytest.fail("Список подсказок пуст")
        suggestions[0].click()

    with allure.step(f"Проверить заголовок страницы (ожидается: {expected_title})"):
        movie_page = MoviePage(main_page.browser)
        assert movie_page.get_movie_title() == expected_title


# Тест 4: Открытие страницы из результатов поиска
@allure.story("Поиск")
@allure.title("Открытие страницы персоны из результатов поиска")
def test_open_from_search_results(main_page):
    """Тест открытия страницы из результатов поиска."""
    with allure.step("Выполнить поиск персоны 'Том Круз'"):
        main_page.search("Том Круз")

    search_page = SearchPage(main_page.browser)
    with allure.step("Выбрать первую персону в результатах"):
        first_person = search_page._wait_for_elements(By.CSS_SELECTOR, "[data-type='person']:first-child")
        first_person.click()

    person_page = PersonPage(main_page.browser)
    with allure.step("Проверить имя персоны"):
        assert "Том Круз" in person_page.get_person_name()


# Тест 5: Оценивание фильма
@allure.story("Оценки")
@allure.title("Оценивание фильма")
@pytest.mark.skip(reason="Требуется авторизация с особыми правами")
def test_rate_movie(main_page):
    """Тест оценки фильма."""
    with allure.step("Открыть страницу фильма 'Форрест Гамп'"):
        movie_page = MoviePage(main_page.browser)
        movie_page.open(448)

    with allure.step("Нажать кнопку 'Оценить'"):
        rate_button = main_page._wait_for_elements(By.CSS_SELECTOR, ".rating-button")
        rate_button.click()

    with allure.step("Выбрать оценку 8"):
        star = main_page._wait_for_elements(By.XPATH, "//div[@class='star'][8]")
        ActionChains(main_page.browser).move_to_element(star).click().perform()


    with allure.step("Проверить установленную оценку"):
        user_rating = main_page._wait_for_elements(By.CSS_SELECTOR, ".user-rating").text
        assert "8" in user_rating


# Тест 6: Оценивание персоны
@allure.story("Оценки")
@allure.title("Добавление персоны в любимые")
@pytest.mark.skip(reason="Требуется авторизация с особыми правами")
def test_rate_person(main_page):
    """Тест добавления персоны в любимые."""
    with allure.step("Открыть страницу персоны 'Леонардо ДиКаприо'"):
        person_page = PersonPage(main_page.browser)
        person_page.open(1900)

    with allure.step("Нажать кнопку 'Любимая звезда'"):
        favorite_button = main_page._wait_for_elements(By.CSS_SELECTOR, "[aria-label='Добавить в любимые звезды']")
        initial_state = favorite_button.get_attribute("aria-checked")
        favorite_button.click()

    with allure.step("Проверить изменение состояния кнопки"):
        new_state = favorite_button.get_attribute("aria-checked")
        assert new_state != initial_state


# Тест 7: Расширенный поиск
@allure.story("Поиск")
@allure.title("Расширенный поиск по жанру и году")
def test_advanced_search(main_page):
    """Тест расширенного поиска."""
    with allure.step("Открыть страницу расширенного поиска"):
        main_page.browser.get(f"{main_url}search/advanced/")

    with allure.step("Установить фильтр: Жанр='комедия', Год='2020-2023'"):
        genre_checkbox = main_page._wait_for_elements(By.XPATH,
                                                      "//span[contains(text(),'комедия')]/preceding-sibling::input")
        genre_checkbox.click()

        year_from = main_page._wait_for_elements(By.NAME, "yearFrom")
        year_from.clear()
        year_from.send_keys("2020")

        year_to = main_page._wait_for_elements(By.NAME, "yearTo")
        year_to.clear()
        year_to.send_keys("2023")

        submit_button = main_page._wait_for_elements(By.CSS_SELECTOR, ".form__submit")
        submit_button.click()

    search_page = SearchPage(main_page.browser)
    with allure.step("Проверить результаты поиска"):
        assert search_page.get_search_results_count() > 0
