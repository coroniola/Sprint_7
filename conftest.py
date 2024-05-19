import pytest
from helpers import Delivery


@pytest.fixture
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
def registration_courier(create_payload):
    courier_data = Delivery.registration_courier(create_payload)
    return courier_data


@pytest.fixture
def generate_payload(create_payload):
    payload = create_payload
    yield payload