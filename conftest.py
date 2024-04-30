import pytest
import requests

from methods import Methods
from user_data import Urls


@pytest.fixture(scope='function')
def create_courier():
    methods = Methods()
    data = methods.register_new_courier_and_return_login_password()
    yield data
    response_post = requests.post(Urls.LOGIN, data={"login": data['login'], "password": data['password']})
    courier_id = response_post.json()['id']
    requests.delete(f'{Urls.DELETE_COURIER}/{courier_id}')
