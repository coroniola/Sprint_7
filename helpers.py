import string
import random
import requests
from settings import Urls
import allure

class Delivery:
    @allure.step("Генерируем данные для курьера (логин, пароль, имя)")

    #метод, который генерирует строку из букв нижнего регистра, длина строки принимается в качестве параметра
    def generate_random_string(len):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(len))
        return random_string


    @allure.step("Получаем данные для регистрации курьера, отправляем запрос на регистрацию")
    def registration_courier(self):
        login_password = []
        login = Delivery.generate_random_string(10)
        password = Delivery.generate_random_string(10)
        name = Delivery.generate_random_string(10)
        payload = {
            'login': login,
            "password": password,
            'name': name
        }
        response = requests.post(Urls.CREATE_COURIER, data=payload)

        if response.status_code == 201:
            login_password = {
                "login": login,
                "password": password,
                "Name": name
            }

        return {'login_pass': login_password, 'response': response}



class TestOrderData:
    ORDER_BODY_DATA = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

class ChangeTestData:
    @staticmethod
    def modify_order_body(key, value):
        body = TestOrderData.ORDER_BODY_DATA.copy()
        body[key] = [value]
        return body