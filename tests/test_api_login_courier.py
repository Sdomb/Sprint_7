import allure
import requests

from variables import Urls


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера')
    def test_login_courier(self, create_courier):
        req = create_courier
        requests.post(Urls.CREATE_COURIER, data=req)
        del req['firstName']
        response = requests.post(Urls.LOGIN, data=req)

        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка авторизации курьера без логина')
    def test_without_login(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        requests.post(Urls.CREATE_COURIER, data=req)
        del req['firstName']
        req['login'] = ''
        response = requests.post(Urls.LOGIN, data=req)

        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации курьера без пароля')
    def test_without_password(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        requests.post(Urls.CREATE_COURIER, data=req)
        del req['firstName']
        req['password'] = ''
        response = requests.post(Urls.LOGIN, data=req)

        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации курьера без логина и пароля')
    def test_without_data(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        requests.post(Urls.CREATE_COURIER, data=req)
        del req['firstName']
        req['password'] = ''
        req['login'] = ''
        response = requests.post(Urls.LOGIN, data=req)

        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации с несуществующими данными')
    def test_fake_login_pass(self):
        response = requests.post(Urls.LOGIN,
                                 data={'login': '&*#^$(*&^#$', 'password': '*(&$TRYGF*(G#(F*#&^T'})

        assert response.status_code == 404 and response.json()['message'] == "Учетная запись не найдена"
