from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import pytest
import time
from selenium.webdriver.common.by import By

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    # Это неявное ожидание, указывается один раз для всех элементов на странице.
    # Драйвер ищет элементы до 10 сек.
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_visible_after_with_implicit_wait(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    visible_after_button = driver.find_element(By.XPATH,'//button[text()="Visible After 5 Seconds"]')
    assert visible_after_button.is_displayed()