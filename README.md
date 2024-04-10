## Восхитительный спринт 'Sprint_7' на тестирование API


### содержание

- [start](#)
- [conftest](#conftest)
- [tests](#tests)
- [allure_results](#allure_results)

### start

####$ Для запуска проекта нужно использовать следующее:

импортировать библиотеки:
pytest, allure, webdriver


для запуска всех автотестов с формированием актуальных отчетов:
```
pytest header_page_test.py order_page_test.py home_page_test.py --alluredir=allure_results
```

открыть в браузере сформированные отчеты:

```
allure serve allure_results 
```


### conftest
Создает класс с методами для тестов


### tests
Здесь лежат тесты


### allure_results
Тут лежат отчеты. 
