import time
import pytest
import allure

from config import USER_LOGIN, USER_PASSWORD
from pages.login_page import LoginPage


pytestmark = pytest.mark.ui


@allure.title("UI 1: Успешный вход в систему")
def test_login_positive(driver):
    if not USER_LOGIN or not USER_PASSWORD:
        pytest.skip("Нет USER_LOGIN/USER_PASSWORD в .env")

    page = LoginPage(driver)
    page.open_login()
    page.login(USER_LOGIN, USER_PASSWORD)

    assert page.is_logged_in(), "Не залогинился (нет маркера logged-in)"


@allure.title("UI 2: Неверный пароль — вход не выполняется")
def test_login_negative_wrong_password(driver):
    if not USER_LOGIN or not USER_PASSWORD:
        pytest.skip("Нет USER_LOGIN/USER_PASSWORD в .env")

    page = LoginPage(driver)
    page.open_login()
    page.login(USER_LOGIN, "WRONG_PASSWORD_123")

    time.sleep(1)
    assert not page.is_logged_in(), "Странно: залогинился с неверным паролем"
    assert page.is_on_login_page(), "Должен остаться на странице логина"


@allure.title("UI 3: После логина остаёмся в logged-in (состояние есть)")
def test_login_shows_logged_in(driver):
    if not USER_LOGIN or not USER_PASSWORD:
        pytest.skip("Нет USER_LOGIN/USER_PASSWORD в .env")

    page = LoginPage(driver)
    page.open_login()
    page.login(USER_LOGIN, USER_PASSWORD)

    assert page.is_logged_in(), "После логина нет logged-in"


@allure.title("UI 4: URL после открытия логина корректный (не улетает на чужой сайт)")
def test_open_login_url_contains_yougile(driver):
    page = LoginPage(driver)
    page.open_login()

    url = page.current_url()
    assert "yougile.com" in url, f"Открыли не Yougile: {url}"


@allure.title("UI 5: После логина URL не пустой и страница открыта")
def test_after_login_url_not_empty(driver):
    if not USER_LOGIN or not USER_PASSWORD:
        pytest.skip("Нет USER_LOGIN/USER_PASSWORD в .env")

    page = LoginPage(driver)
    page.open_login()
    page.login(USER_LOGIN, USER_PASSWORD)

    assert page.current_url(), "URL пустой после действий"
