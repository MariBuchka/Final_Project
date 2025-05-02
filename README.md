# Final_Project

Данная работа является продолжением [проекта](https://bugs-not-bunny.yonote.ru/share/f4cfc0e2-4359-4fb7-9558-85ef90e19b56) по ручному тестированию сайта _Кинопоиск_. Некоторые manual тесты в процессе были переработаны.

#### **Основная задача работы**: _автоматизировать UI- и API-тесты из финальной работы по ручному тестированию._

### Структура проекта

```commandline
Final_Project/

├── config/                    # Конфигурационные файлы
│   ├── __init__.py
│   ├── config.py              # Основные настройки (URL, куки и т.д.)
│   └── baseAPI.py             # Базовые настройки для API тестов
│
├── pages/                     # Page Object Model
│   ├── __init__.py
│   ├── APIGetMovie.py         # API методы получения информации о фильмах/сериалах
│   ├── APIGetPerson.py        # API методы получения информации о персонах
│   ├── APISearchMovies.py     # API методы поиска фильмов/сериалов
│   ├── APISearchMovies.py     # API методы поиска персон
│   ├── UIAdvancedSearch.py    # Страница расширенного поиска
│   ├── UIDirectorPage.py      # Страница режиссера
│   ├── UIMoviePage.py         # Страница фильма
│   ├── UIPersonPage.py        # Страница персоны
│   └── UITopCollection.py     # Страница подборок
│
├── test/                      # Тесты
│   ├── __init__.py
│   ├── test_api.py            # API-тесты
│   └── test_ui.py             # UI-тесты
│
├── .gitignore                 # Игнорируемые файлы для Git
├── README.md                  # Документация проекта
├── requirements.txt           # Зависимости Python
└── pytest.ini                 # Конфигурация Pytest
```

### Команды для запуска тестов и формирования отчетов:

- Запуск тестов API по команде: `python -m pytest test_api.py --alluredir allure-result`
- Запуск тестов UI по команде: `python -m pytest test_ui.py --alluredir allure-result`
- Запуск всех тестов: `python -m pytest --alluredir allure-result`
- Генерация отчета по команде: `allure serve allure-result`

### Описание базового синтаксиса и технологий

Проект использует следующий стек технологий (см. `requirements.txt`):

1. **Page Object Model**: паттерн проектирования тестов;
2. **Python 3.13**: основной язык реализации тестов;
3. **Pytest**: фреймворк для организации тестов;
4. **Requests 2.32**: для выполнения HTTP-запросов и тестирования API;
5. **Selenium 4.28**: для автоматизации веб-взаимодействий;
6. **Allure Report**: для генерации детализированных отчетов.

### Форматирование кода

- Код форматируется в соответствии с PEP 8 (стиль написания кода на Python).
- Используются docstrings для документирования методов и функций.
- Все шаги теста размечаются с помощью `@allure.step` или `with allure.step` для улучшения читаемости отчетов.

### Основные шаги
1. Склонировать проект.
2. Добавить API токен и cookies в файл `config.py`.
3. Установить зависимости.
4. Запустить тесты `pytest`.

### Команды для установки библиотек

`pip install pytest`

`pip install selenium`

`pip install webdriver-manager#Final_Project`

#### P.S. Команды написаны под OS Win и WebDraiver GH. При необходимости следует заменить команды на соответствующие Вашему окружению.

---