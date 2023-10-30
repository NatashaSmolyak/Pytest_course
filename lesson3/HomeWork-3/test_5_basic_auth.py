from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

"""2. Необходимо пройти базовую авторизацию"""
def test_5_basic_auth(driver):
    driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth/')
    con_text = driver.find_element(By.XPATH, "//p[contains(text(),'Congratulations! You must have the proper credentials.')]")
    assert con_text.text == 'Congratulations! You must have the proper credentials.'
