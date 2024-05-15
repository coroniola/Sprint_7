import allure
import requests
from settings import Urls
from helpers import Delivery



class TestCourierAuthorize:
    @allure.title("Проверка успешной авторизации созданного курьера")
    def test_authorize_courier_successful(self, registration_courier):
        payload = {
            "login": registration_courier['login_password']['login'],
            "password": registration_courier['login_password']['password']
        }
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 200 and 'id' in response.text


    @allure.title("Проверка авторизации несуществующего курьера")
    def test_authorize_non_existent_courier(self):
        login = Delivery.generate_random_string(10)
        password = Delivery.generate_random_string(10)
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 404 and  response.json().get('message')== "Учетная запись не найдена"

    @allure.title('Проверка авторизации без логина')
    def test_authorize_without_login(self,  registration_courier):
        payload = {
            "password":  registration_courier['login_password']['password']
        }
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 400 and response.json().get('message')== "Недостаточно данных для входа"

    @allure.title('Проверка авторизации без пароля')
    def test_authorize_without_password(self,  registration_courier):
        payload = {
            "login": registration_courier['login_password']['login'],
        }
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 400 and response.json().get('message')== "Недостаточно данных для входа"