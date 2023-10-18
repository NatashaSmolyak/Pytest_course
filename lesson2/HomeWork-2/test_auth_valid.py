from selenium.webdriver.common.by import By
import time
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from data import LOGIN_VALID, PASSWORD_VALID, MAIN_PAGE, INVENTORY_PAGE

def test_login_form_valid(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN_VALID)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD_VALID)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    time.sleep(2)
    assert driver.current_url == INVENTORY_PAGE


