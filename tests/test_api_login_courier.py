import allure
import requests


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера')
    def test_login_courier(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=req)
        req.pop('firstName')
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=req)

        assert response.status_code == 200 and 'id' in response.text
        methods.delete_courier(req['login'], req['password'])

    @allure.title('Проверка авторизации курьера без логина')
    def test_without_login(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=req)
        req.pop('firstName')
        req['login'] = ''
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=req)

        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации курьера без пароля')
    def test_without_password(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=req)
        req.pop('firstName')
        req['password'] = ''
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=req)

        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации курьера без логина и пароля')
    def test_without_data(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=req)
        req.pop('firstName')
        req['password'] = ''
        req['login'] = ''
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=req)

        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации с несуществующими данными')
    def test_fake_login_pass(self):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data={'login': '&*#^$(*&^#$', 'password': '*(&$TRYGF*(G#(F*#&^T'})

        assert response.status_code == 404 and response.json()['message'] == "Учетная запись не найдена"
