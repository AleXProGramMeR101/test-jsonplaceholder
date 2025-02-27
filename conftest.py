import pytest
import requests

# Фикстура с базовым api url
@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

# Фикстура для сессии http-запросов
@pytest.fixture(scope="session")
def session():
    return requests.Session()