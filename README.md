<<<<<<< HEAD
# Sprint_6 — Автоматизация тестирования сервиса «Самокат»

## Описание проекта

Проект содержит автоматизированные UI-тесты для сервиса заказа самокатов.

Сайт: https://qa-scooter.praktikum-services.ru/

## Используемые технологии

- Python
- Selenium WebDriver
- Pytest
- Allure


## Запуск тестов

Запустить все тесты:

```bash
python -m pytest -v
```

## Формирование Allure-отчёта

Запустить тесты с сохранением результатов Allure:

```bash
python -m pytest --alluredir=allure-results
```

Сформировать HTML-отчёт:

```bash
allure generate allure-results --clean -o allure-report
```

Открыть отчёт:

```bash
allure open allure-report
```
=======
Автоматизация тестирования сервиса «Самокат»
>>>>>>> origin/main
