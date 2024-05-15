import allure
import requests
from settings import Urls

class TestGetOrderList:
    @allure.title('Проверка получения списка заказов')
    def test_get_order_list(self):
        response = requests.get(Urls.ORDER)
        assert response.status_code == 200 and response.json()["orders"] != []
