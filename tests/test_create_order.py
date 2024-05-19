import requests
import allure
from settings import Urls
from helpers import ChangeTestData
import pytest

class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа с различными цветами')
    @pytest.mark.parametrize('color', [None, ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_success_create_order(self, color):
        payload = ChangeTestData.modify_order_body("color", color)
        response = requests.post(Urls.ORDER, json=payload)
        assert response.status_code == 201 and 'track' in response.text