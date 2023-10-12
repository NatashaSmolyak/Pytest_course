from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# 2. Удаление единственного товара из корзины через корзину
def test_remove_item():
    driver.get("https://www.saucedemo.com/")
    # Авторизация
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(3)

    # Сохранение в переменную text_before названия добавляемого товара
    text_before = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > div").text

    # Добавление в корзину
    button_add = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    button_add.click()
    time.sleep(2)

    # Переход в корзину
    shopping_cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    shopping_cart.click()
    time.sleep(2)

    # Сохранение в переменную text_after названия добавленного товара
    text_after = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > div").text
    assert text_before == text_after
    time.sleep(2)

    # Удаление из корзины
    remove = driver.find_element(By.XPATH, "//button[@data-test = 'remove-sauce-labs-backpack']")
    remove.click()

    # Сохранение в переменную removed наличие класса removed_cart_item
    removed = driver.find_element(By.CSS_SELECTOR, ".removed_cart_item")
    assert removed
    time.sleep(3)
