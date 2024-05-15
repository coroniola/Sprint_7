import requests
import pytest
from settings import Urls
import allure
from helpers import Delivery


def create_payload():
    login = Delivery.generate_random_string(10)
    password = Delivery.generate_random_string(10)
    name = Delivery.generate_random_string(10)

    return {
        "login": login,
        "password": password,
        "name": name
    }

@pytest.fixture
@allure.step("Получаем данные для регистрации курьера, отправляем запрос на регистрацию")

def registration_courier():
    login_password = []
    payload = create_payload()
    response = requests.post(Urls.CREATE_COURIER, data=payload)

    if response.status_code == 201:
        login_password = {
            "login": payload['login'],
            "password": payload['password'],
            "name": payload['name']
        }

    return {'login_password': login_password, 'response': response}

@pytest.fixture
def generate_payload():
    payload = create_payload()
    yield payload