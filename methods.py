import allure
import requests
import random
import string


class Methods:

    @allure.step('Генерируем данные курьера и возвращаем словарь с данными')
    def register_new_courier_and_return_login_password(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return payload

    @allure.step('Удаляем курьера')
    def delete_courier(self, login, password):
        response_post = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={
            "login": login,
            "password": password,
        })
        courier_id = response_post.json()['id']
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/:id{courier_id}')
