from selenium.webdriver.common.by import By
import time
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON, ERROR
from data import MAIN_PAGE, LOGIN_INVALID, PASSWORD_INVALID, VALUE_ERROR_EXPECTED

def test_login_form_invalid(driver):
    driver.get(MAIN_PAGE)
    text_error_expected = 'Epic sadface: Username and password do not match any user in this service'
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN_INVALID)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD_INVALID)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    error_actual = driver.find_element(By.XPATH, ERROR)
    value_error_actual = error_actual.text
    time.sleep(2)
    assert VALUE_ERROR_EXPECTED == value_error_actual
