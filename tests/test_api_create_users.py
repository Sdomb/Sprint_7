import allure
import requests


class TestCreateUser:

    @allure.title('Проверка создания курьера со всеми обязательными полями')
    def test_create_user(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        resp = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=req)
        login, password = list(req.values())[:2]

        assert resp.status_code == 201 and resp.text == '{"ok":true}'
        methods.delete_courier(login, password)

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_create_two_same_user(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=req)
        two_user = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=req)

        assert two_user.status_code == 409 \
               and two_user.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка создания курьера без логина')
    def test_not_present_fields(self, methods):

        req = methods.register_new_courier_and_return_login_password()
        req.pop('login')
        fail_user = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=req)

        assert fail_user.status_code == 400 \
               and fail_user.json()['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка создания курьера без пароля')
    def test_not_present_fields(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        req.pop('password')
        fail_user = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=req)

        assert fail_user.status_code == 400 \
               and fail_user.json()['message'] == "Недостаточно данных для создания учетной записи"
