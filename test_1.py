import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


def test_1():
    options = ChromeOptions()
    options.headless = True
    driver = Chrome(options=options)
    driver.get('https://go.skillbox.ru/')
    assert 'Обучающая онлайн-платформа Skillbox' == driver.title
    time.sleep(3)
    driver.quit()