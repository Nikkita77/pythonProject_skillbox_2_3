import time
import pytest
import allure
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


class TestExample:  # Teстовый набор
    @allure.description("Test open url")
    def test_1(self, set_up):
        with allure.step("open url"):
            options = ChromeOptions()
            # options.headless = True
            driver = Chrome(options=options)
            driver.get('https://go.skillbox.ru/')
            assert 'Skillbox' == driver.title
            driver.quit()

    def test_2(self, set_up):
        options = ChromeOptions()
        # options.headless = True
        driver = Chrome(options=options)
        driver.get('https://go.skillbox.ru/')
        assert 'Skillbox' == driver.title
        driver.quit()

    def test_3(self, set_up):
        options = ChromeOptions()
        # options.headless = True
        driver = Chrome(options=options)
        driver.get('https://go.skillbox.ru/')
        assert 'Skillbox' == driver.title
        driver.quit()




