import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from api.client import ApiClient
from config import API_BASE_URL, API_TOKEN


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.delete_all_cookies()

    yield driver

    driver.quit()


@pytest.fixture
def api_client() -> ApiClient:
    if not API_BASE_URL:
        pytest.skip("Нет API_BASE_URL в .env")
    if not API_TOKEN:
        pytest.skip("Нет API_TOKEN в .env")
    return ApiClient(base_url=API_BASE_URL, token=API_TOKEN)
