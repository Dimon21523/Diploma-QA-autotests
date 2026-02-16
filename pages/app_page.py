import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AppPage(BasePage):
    LOGOUT_BUTTONS = [
        (
            By.XPATH,
            "//*[contains(., 'Выйти')]/ancestor::*[self::button or self::a][1]",
        ),
        (
            By.XPATH,
            "//*[contains(., 'Logout')]/ancestor::*[self::button or self::a][1]",
        ),
        (
            By.CSS_SELECTOR,
            "[data-testid*='logout' i]",
        ),
    ]

    PROFILE_MENU = [
        (
            By.CSS_SELECTOR,
            "[data-testid*='user' i]",
        ),
        (
            By.CSS_SELECTOR,
            "[data-testid*='profile' i]",
        ),
        (
            By.XPATH,
            "//*[contains(@class,'avatar') or contains(@class,'profile')]",
        ),
    ]

    def open_profile_menu_if_any(self) -> None:
        el = self.find_first(self.PROFILE_MENU, timeout=3)
        if el:
            try:
                el.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", el)
            time.sleep(0.3)

    def logout(self) -> None:
        self.open_profile_menu_if_any()

        btn = self.find_first(self.LOGOUT_BUTTONS, timeout=5)
        if btn is None:
            raise AssertionError("Не нашёл кнопку Logout/Выйти")

        try:
            btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", btn)
