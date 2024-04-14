import allure
import requests
from variables import TextMessages, Urls


class TestCreateUser:

    @allure.title('Проверка создания курьера со всеми обязательными полями')
    def test_create_user(self, create_courier):

        resp = requests.post(Urls.CREATE_COURIER, data=create_courier)
        assert resp.status_code == 201 and resp.text == TextMessages.OK_CREATE

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_create_two_same_user(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        requests.post(Urls.CREATE_COURIER, data=req)
        two_user = requests.post(Urls.CREATE_COURIER, data=req)

        assert two_user.status_code == 409 \
               and two_user.json()['message'] == TextMessages.LOGIN_BUSY

    @allure.title('Проверка создания курьера без логина')
    def test_not_present_fields_login(self, methods):

        req = methods.register_new_courier_and_return_login_password()
        del req['login']
        fail_user = requests.post(Urls.CREATE_COURIER, data=req)

        assert fail_user.status_code == 400 \
               and fail_user.json()['message'] == TextMessages.INSUFFICIENT_DATA

    @allure.title('Проверка создания курьера без пароля')
    def test_not_present_fields_pass(self, methods):
        req = methods.register_new_courier_and_return_login_password()
        del req['password']
        fail_user = requests.post(Urls.CREATE_COURIER, data=req)

        assert fail_user.status_code == 400 \
               and fail_user.json()['message'] == TextMessages.INSUFFICIENT_DATA
