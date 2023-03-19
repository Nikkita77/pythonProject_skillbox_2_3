import time
import pytest
import allure
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


@allure.step('Проверка заголовка страницы')
def check_title(driver, title):
    assert title == driver.title


class TestExample:  # Teстовый набор
    @allure.description("Test open url")
    def test_1(self, set_up):  # Тест-кейс
        with allure.step("open url"):
            options = ChromeOptions()
            # options.headless = True
            driver = Chrome(options=options)
            driver.get('https://go.skillbox.ru/')
            check_title(driver=driver, title='Обучающая онлайн-платформа Skillbox')
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
