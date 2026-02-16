import time
from typing import Optional

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from config import URL_UI
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUTS = [
        (By.CSS_SELECTOR, "input[type='email']"),
        (By.CSS_SELECTOR, "input[name='email']"),
        (
            By.XPATH,
            "//input[contains(@placeholder,'mail') or "
            "contains(@placeholder,'E-mail') or "
            "contains(@placeholder,'Email')]",
        ),
    ]

    PASSWORD_INPUTS = [
        (By.CSS_SELECTOR, "input[type='password']"),
        (By.CSS_SELECTOR, "input[name='password']"),
        (
            By.XPATH,
            "//input[contains(@placeholder,'Пароль') or "
            "contains(@placeholder,'Password')]",
        ),
    ]

    SUBMIT_BUTTONS = [
        (By.XPATH, "//button[normalize-space()='Войти']"),
        (By.XPATH, "//button[contains(normalize-space(.), 'Войти')]"),
        (
            By.XPATH,
            "//*[normalize-space()='Войти' or "
            "contains(normalize-space(.),'Войти')]/ancestor::button[1]",
        ),
        (
            By.XPATH,
            "//*[@role='button' and "
            "(normalize-space()='Войти' or contains(.,'Войти'))]",
        ),
        (By.CSS_SELECTOR, "button[type='submit']"),
        (By.CSS_SELECTOR, "input[type='submit']"),
        (By.CSS_SELECTOR, "[data-testid*='login' i]"),
        (By.CSS_SELECTOR, "[data-testid*='sign' i]"),
    ]

    LOGGED_MARKERS = [
        (By.CSS_SELECTOR, "body.logged-in"),
        (By.XPATH, "//body[contains(@class,'logged-in')]"),
    ]

    def open_login(self) -> None:
        if not URL_UI:
            raise AssertionError("URL_UI пустой. Заполни URL_UI в .env")
        self.open_url(URL_UI)

    def login(self, email: str, password: str) -> None:
        with allure.step("Ввести email"):
            email_el: Optional[WebElement] = self.find_first(
                self.EMAIL_INPUTS,
                timeout=15,
            )
            if email_el is None:
                raise AssertionError("Не нашёл поле email")
            email_el.clear()
            email_el.send_keys(email)

        with allure.step("Ввести пароль"):
            pass_el: Optional[WebElement] = self.find_first(
                self.PASSWORD_INPUTS,
                timeout=15,
            )
            if pass_el is None:
                raise AssertionError("Не нашёл поле пароль")
            pass_el.clear()
            pass_el.send_keys(password)

            pass_el.send_keys(Keys.TAB)
            time.sleep(0.2)

        with allure.step("Нажать кнопку 'Войти'"):
            btn: Optional[WebElement] = self.find_first(
                self.SUBMIT_BUTTONS,
                timeout=15,
            )

            if btn is None:
                pass_el.send_keys(Keys.ENTER)
                return

            try:
                btn.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", btn)

    def is_logged_in(self) -> bool:
        marker = self.find_first(self.LOGGED_MARKERS, timeout=5)
        return marker is not None

    def is_on_login_page(self) -> bool:
        return self.find_first(self.EMAIL_INPUTS, timeout=3) is not None

    def current_url(self) -> str:
        return self.driver.current_url
