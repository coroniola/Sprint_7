import requests
import allure
from settings import Urls
from expected_data import ExpectedMessages

class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    def test_create_courier_successful(self, registration_courier):
        response = registration_courier['response']
        assert response.status_code == 201
        assert response.json()['ok'] is True

    @allure.title('Проверка невозможности повторной регистрации курьера с теми же данными')
    def  test_create_courier_with_existing_credentials(self, registration_courier):
        login, password, name = (
            registration_courier['login_password']['login'],
            registration_courier['login_password']['password'],
            registration_courier['login_password']['name']
        )

        payload = {
            "login": login,
            "password": password,
            "name": name
        }

        response = requests.post(Urls.CREATE_COURIER, data=payload)
        expected_message = ExpectedMessages.COURIER_EXISTING_LOGIN_MESSAGE
        assert response.status_code == 409
        assert response.json().get('message') == expected_message

    @allure.title('Регистрация курьера без имени')
    def test_create_courier_without_name(self, generate_payload):
        payload = generate_payload
        del payload['name']
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Регистрация курьера без логина')
    def test_create_courier_without_login(self, generate_payload):
        payload = generate_payload
        expected_message = ExpectedMessages.COURIER_REG_INCOMPLETE_DATA_MESSAGE
        del payload['login']
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.json().get('message') == expected_message

    @allure.title('Регистрация курьера без пароля')
    def test_create_courier_without_login(self, generate_payload):
        payload = generate_payload
        expected_message = ExpectedMessages.COURIER_REG_INCOMPLETE_DATA_MESSAGE
        del payload['password']
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.json().get(
            'message') == expected_message



