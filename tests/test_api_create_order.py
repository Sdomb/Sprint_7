import allure
import pytest
import requests


class TestCreateOrder:
    person_data = [
        ['Гиви', 'Владимирович', 'Абакан, ул. Новинского', '42', '+7 800 555 35 35', '12', '2020-06-06',
         'Эхма вот поеду ка я', "BLACK"],
        ['Владилен', 'Мойшевич', 'Гомель, главная площадь', '6', '+7 800 555 35 35', '3', '2020-06-06',
         'Красота в глазах смотрящего', "GREY"],
        ['Гвиневра', 'Стулова', 'Лиссабон, около моста', '12', '+7 800 555 35 35', '11', '2020-06-06',
         'Из пруда не вытащишь', "BLACK, GREY"],
        ['Сэмуэль', 'Эйджексон', 'Стрелитамак, Аптекарский переулок .', '3', '+7 800 555 35 35', '1', '2020-06-06',
         'Два сапога', ""]

    ]

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
        resp = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=data)
        assert resp.status_code == 201
        assert 'track' in resp.text
