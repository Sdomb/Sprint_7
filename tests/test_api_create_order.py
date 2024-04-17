import allure
import pytest
import requests
from user_data import TextMessages, Urls


class TestCreateOrder:
    person_data = TextMessages.person_data

    @pytest.mark.parametrize(
        "firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color", person_data)
    @allure.title('Создание заказа с цветом и без него')
    def test_create_order_with_color(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate,
                                     comment, color):
        data = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": [color],
        }
        resp = requests.post(Urls.CREATE_ORDERS, json=data)
        assert resp.status_code == 201
        assert 'track' in resp.text
