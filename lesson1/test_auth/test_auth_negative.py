from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#Авторизация, используя некорректные данные (neg_user, neg_user)

def test_login_form_invalid():
    driver.get("https://www.saucedemo.com/")
    url_before = driver.current_url
    text_error_expected = 'Epic sadface: Username and password do not match any user in this service'

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("neg_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("neg_user")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(2)

    error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    value_error = error.text
    time.sleep(2)
    assert value_error == "Epic sadface: Username and password do not match any user in this service"
