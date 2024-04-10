import allure
import requests


class TestListOrders:

    @allure.title('Проверка получения списка заказа')
    def test_list_orders(self):
        resp = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        assert resp.status_code == 200 and 'orders' in resp.text
