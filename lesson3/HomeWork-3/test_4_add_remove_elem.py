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
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Проверка, что элемент отсутствует на странице.
def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return True
    return False

""" 1. Необходимо создать и удалить элемент"""
def test_4_add_remove(driver):
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    add = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    add.click()
    delete = driver.find_element(By.XPATH, "//button[@onclick='deleteElement()']")
    assert delete.is_displayed()

    delete.click()
    removed = check_exists_by_xpath(driver, "//button[@onclick='deleteElement()']")
    assert removed == True

