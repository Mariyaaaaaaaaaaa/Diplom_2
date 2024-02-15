# Diplom_2

# Тест-сьют для проверки API приложения "Stellar Burgers" с помощью Pytest и библиотеки Requests

## Файлы:
- tests/ - папка с файлами тестов:
- tests/test_user_create.py - тесты эндпойнта создания пользователя
- tests/test_user_login.py  - тесты эндпойнта авторизации курьера
- tests/test_user_change_data.py   - тесты эндпойнта создания заказа
- tests/test_order_create.py - тесты эндпойнта получения списка заказов
- tests/test_order_get.py - тесты эндпойнта удаления курьера

- helpers/ - файл с базовыми методами для работы с запросами и методы проверок
- conftest.py - содержит фикстуры для создания и удаления пользователя, создания заказов 
- data.py - константы и данные для тестов
- urls.py - файл с URL-адресами


- .gitignore - файл для проекта в Git/GinHub
- requirements.txt - файл с внешними зависимостями
- README.md - файл с описанием проекта (этот файл)


## Для запуска тестов должны быть установлены пакеты:
- pytest,
- requests, 
- allure-pytest и
- allure-python-commons.

## Для генерации отчетов необходимо дополнительно установить:
- фреймворк Allure,
- JDK

## Запуск всех тестов выполняется командой:

    pytest -v ./tests

Запуск тестов с генерацией отчета Allure выполняется командой:

    pytest -v ./tests  --alluredir=allure_results

Генерация отчета выполняется командой:

    allure serve allure_results

Генерация файла внешних зависимостей requirements.txt выполняется командой:

    pip freeze > requirements.txt

Установка зависимостей из файла requirements.txt выполняется командой:

    pip install -r requirements.txt

