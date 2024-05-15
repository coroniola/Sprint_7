import requests
import allure
from settings import Urls


class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    def test_create_courier_successful(self, registration_courier):
        assert registration_courier['response'].status_code == 201 and registration_courier['response'].text == '{"ok":true}'

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
            "Name": name
        }

        response = requests.post(Urls.CREATE_COURIER, data=payload)
        expected_message = "Этот логин уже используется. Попробуйте другой."

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
        del payload['login']
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.json().get('message')== "Недостаточно данных для создания учетной записи"

    @allure.title('Регистрация курьера без пароля')
    def test_create_courier_without_login(self, generate_payload):
        payload = generate_payload
        del payload['password']
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.json().get(
            'message') == "Недостаточно данных для создания учетной записи"



