import allure
import requests

from variables import Urls


class TestListOrders:

    @allure.title('Проверка получения списка заказа')
    def test_list_orders(self):
        resp = requests.get(Urls.RECEIVING_ORDERS)
        assert resp.status_code == 200 and 'orders' in resp.text
