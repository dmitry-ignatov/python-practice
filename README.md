# Python Practice

Репозиторий с практическими проектами, которые я делал по мере изучения Python. Здесь сохранён весь путь: от небольших консольных программ до работы с тестами, REST API, FastAPI и SQLite.

## Избранные проекты

### [16_task_api_sqlite](16_task_api_sqlite)
REST API для управления задачами на FastAPI с хранением данных в SQLite.

Что есть в проекте: CRUD, Pydantic-модели, HTTP-ошибки, параметрические SQL-запросы, инициализация базы через lifespan и тестирование через pytest/TestClient с отдельной временной БД.

**Стек:** Python, FastAPI, SQLite, pytest.

### [12_json_config_validator](12_json_config_validator)
Валидатор JSON-конфигурации с проверкой обязательных полей, типов и допустимых значений.

В проекте отдельно обрабатываются ошибки файла и структуры данных, а основная логика покрыта 25 тестовыми сценариями.

**Стек:** Python, JSON, pathlib, pytest.

### [14_weather_reporter](14_weather_reporter)
Консольная программа, которая сначала получает координаты города через Open-Meteo Geocoding API, а затем запрашивает текущую погоду и прогноз.

Есть обработка сетевых ошибок, HTTP-ответов и неизвестных погодных кодов. Основная логика проверяется автоматическими тестами.

**Стек:** Python, requests, REST API, JSON, pytest.

### [05_duplicate_finder](05_duplicate_finder)
Поиск одинаковых файлов во вложенных папках.

Сначала файлы группируются по размеру, затем потенциальные совпадения сравниваются по SHA-256. Файлы читаются блоками, поэтому большие файлы не загружаются в память целиком.

**Стек:** Python, pathlib, hashlib.

## Все проекты

| № | Проект | Что делает |
|---|---|---|
| 01 | [Expense Analyzer](01_expense_analyzer) | Учёт расходов, статистика, сохранение и загрузка данных |
| 02 | [File Sorter](02_file_sorter) | Распределение имён файлов по категориям |
| 03 | [Text Cleaner](03_text_cleaner) | Очистка, нормализация и сортировка строк |
| 04 | [Folder Reporter](04_folder_reporter) | Анализ содержимого папки и создание отчёта |
| 05 | [Duplicate Finder](05_duplicate_finder) | Поиск дубликатов файлов по размеру и SHA-256 |
| 06 | [Personal Task Tracker](06_personal_task_tracker) | Менеджер задач с хранением в JSON |
| 07 | [Notes Database](07_notes_database) | CRUD-приложение для заметок на SQLite |
| 08 | [Book Catalog](08_book_catalog) | Каталог книг с поиском и хранением в SQLite |
| 09 | [Password Checker](09_password_checker) | Проверка надёжности пароля |
| 10 | [Text Report Analyzer](10_text_report_analyzer) | Анализ текстовых файлов и формирование отчёта |
| 11 | [Log Analyzer](11_log_analyzer) | Разбор и фильтрация логов |
| 12 | [JSON Config Validator](12_json_config_validator) | Валидация JSON и автоматические тесты |
| 13 | [GitHub Repo Reporter](13_github_repo_reporter) | Работа с GitHub REST API |
| 14 | [Weather Reporter](14_weather_reporter) | Два последовательных API-запроса и прогноз погоды |
| 15 | [Task API](15_task_api) | REST API на FastAPI с хранением в памяти |
| 16 | [Task API SQLite](16_task_api_sqlite) | FastAPI + SQLite + тестовая база |

## Технологии

Python, pytest, requests, REST API, FastAPI, Pydantic, SQLite, SQL, JSON, pathlib, Git.

У каждого проекта есть свой README с описанием запуска и основных возможностей.