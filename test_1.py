import time
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


class TestExample:  # Teстовый набор
    def test_1(self, set_up):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.get('https://go.skillbox.ru/')
        assert 'Обучающая онлайн-платформа Skillbox' == driver.title
        time.sleep(3)
        driver.quit()

    def test_2(self, set_up):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.get('https://go.skillbox.ru/')
        assert 'Обучающая онлайн-платформа Skillbox' == driver.title
        time.sleep(3)
        driver.quit()

    def test_3(self, set_up):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.get('https://go.skillbox.ru/')
        assert 'Обучающая онлайн-платформа Skillbox' == driver.title
        time.sleep(3)
        driver.quit()




