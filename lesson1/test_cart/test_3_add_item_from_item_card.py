from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

# 3. Добавление товара в корзину из карточки товара
def test_add_item_from_item_card():
    driver.get("https://www.saucedemo.com/")
    # Авторизация
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # Сохранение в переменную text_main названия добавляемого товара
    text_main = driver.find_element(By.CSS_SELECTOR, "a[id = 'item_4_title_link'] > div[class='inventory_item_name']").text
    # Переход в карточку товара
    item_link = driver.find_element(By.CSS_SELECTOR, "a[id = 'item_4_title_link'] > div[class='inventory_item_name']")
    item_link.click()
    time.sleep(2)

    # Сохранение в переменную text_card названия товара, написанного в карточке
    text_card = driver.find_element(By.XPATH, "//div [contains(text(),'Sauce Labs Backpack')]").text
    time.sleep(2)

    # Добавление в корзину
    button_add = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    button_add.click()
    time.sleep(2)

    # Переход в корзину
    shopping_cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    shopping_cart.click()
    time.sleep(2)

    # Сохранение в переменную text_after названия добавленного товара
    text_after = driver.find_element(By.CSS_SELECTOR, "a[id = 'item_4_title_link'] > div[class='inventory_item_name']").text
    assert text_main == text_card == text_after
    time.sleep(2)

