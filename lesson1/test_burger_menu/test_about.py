from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# 2. Проверка работоспособности кнопки "About" в меню
def test_about():
    driver.get("https://www.saucedemo.com/")

    url_before = driver.current_url

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(2)

    about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
    about.click()

    url_about = driver.current_url
    assert url_about == 'https://saucelabs.com/'