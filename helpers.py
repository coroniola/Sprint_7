import string
import random
import requests
from settings import Urls
import allure
from data import TestOrderData
class Delivery:
    @allure.step("Генерируем данные для курьера (логин, пароль, имя)")

    #метод, который генерирует строку из букв нижнего регистра, длина строки принимается в качестве параметра
    def generate_random_string(len):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(len))
        return random_string

    @staticmethod
    @allure.step("Получаем данные для регистрации курьера, отправляем запрос на регистрацию")
    def registration_courier(courier_data):
        login_password = []
        payload = courier_data
        response = requests.post(Urls.CREATE_COURIER, data=payload)

        if response.status_code == 201:
            login_password = {
                "login": payload['login'],
                "password": payload['password'],
                "name": payload['name']
            }

        return {'login_password': login_password, 'response': response}

class ChangeTestData:
    @staticmethod
    def modify_order_body(key, value):
        body = TestOrderData.ORDER_BODY_DATA.copy()
        body[key] = [value]
        return body