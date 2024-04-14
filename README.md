## Восхитительный спринт 'Sprint_7' на тестирование API


### содержание

- [start](#)
- [conftest](#conftest)
- [tests](#tests)
- [allure_results](#allure_results)
- [variables](#variables)

### start

####$ Для запуска проекта нужно использовать следующее:

импортировать библиотеки:
pytest, allure, webdriver


для запуска всех автотестов с формированием актуальных отчетов:
```
pytest test_api_create_order.py test_api_create_users.py test_api_list_orders.py test_api_login_courier.py --alluredir=allure_results
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

###  variables
В этот файл вынесены данные, которые переиспользуются в разных тестах.
Есть урлы для апи и текста проверок.