from __future__ import annotations

from typing import Optional, Sequence, Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def wait_visible(self, locator: Locator, timeout: int = 15) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator: Locator, timeout: int = 15) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def find_first(
        self,
        locators: Sequence[Locator],
        timeout: int = 10,
    ) -> Optional[WebElement]:
        for loc in locators:
            try:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(loc)
                )
            except Exception:
                continue
        return None
