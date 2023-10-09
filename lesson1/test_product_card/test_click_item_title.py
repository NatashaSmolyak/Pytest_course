from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# 1. Успешный переход к карточке товара после клика на название товара
def test_transition_to_item_card_after_click_title():
    driver.get("https://www.saucedemo.com/")
    # Авторизация
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # Сохранение в переменную text_main названия товара, на карточку которого совершается переход
    text_main = driver.find_element(By.CSS_SELECTOR, "a[id = 'item_4_title_link'] > div[class='inventory_item_name']").text

    # Переход в карточку товара
    link_item_title = driver.find_element(By.CSS_SELECTOR, "a[id = 'item_4_title_link'] > div[class='inventory_item_name']")
    link_item_title.click()
    time.sleep(2)

    # Сохранение в переменную text_card названия товара, написанного в карточке
    text_card = driver.find_element(By.XPATH, " //div[@class='inventory_details_name large_size']").text
    #print(text_card)
    time.sleep(2)

    assert text_main == text_card

    driver.quit()