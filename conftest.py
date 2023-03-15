from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


import pytest
from selenium.webdriver import Chrome

@pytest.fixture() #  вариант для каждого теста
def set_up():
    print("Start test")
    yield
    print("Finish test")