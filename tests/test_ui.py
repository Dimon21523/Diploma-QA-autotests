import pytest
import allure
from pages.login_page import LoginPage
from config import URL


@allure.epic("UI Тестирование")
@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Успешный вход в систему")
    @allure.description("Тест проверяет вход с валидными данными")
    @pytest.mark.ui
    def test_login_positive(self, driver):
        page = LoginPage(driver)
        
        with allure.step("Открытие главной страницы"):
            page.open_url(URL)

        page.enter_username("standard_user")
        page.enter_password("secret_sauce")
        page.click_login()

        with allure.step("Проверка успешного входа (наличие слова 'products' в URL)"):
            assert "inventory" in driver.current_url
