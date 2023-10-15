# 3. Проверка работоспособности фильтра (low to high)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

driver = webdriver.Chrome()

def test_filter_3():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # Формируем изначальный список цен на странице
    items_price_before = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    # Парсим (.text) цены в список, обрезаем знак валюты ([1:]), преобразуем список в вещественный тип данных
    values_items_price_before = [float(items_price_before[i].text[1:]) for i in range(len(items_price_before))]
    #  Сортируем список цен по возрастанию
    sort_values_items_price_before = sorted(values_items_price_before)
    time.sleep(3)

    # Находим фильтр, с помощью Keys.PAGE-DOWN, Keys.UP выбираем предпоследний пункт списка, клавиша ENTER (Keys.RETURN)
    filter = driver.find_element(By.XPATH, "//select[@data-test ='product_sort_container']")
    filter.click()
    time.sleep(2)
    filter.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    filter.send_keys(Keys.UP)
    filter.send_keys(Keys.RETURN)
    time.sleep(3)

    # Формируем список цен после использования фильтра "low to high"
    sort_items_price_after = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    # Парсим (.text) список цен, обрезаем знак валюты [1:]
    sort_values_items_price_after = [float(sort_items_price_after[i].text[1:]) for i in range(len(sort_items_price_after))]
    # Сравниваем два списка
    assert sort_values_items_price_before == sort_values_items_price_after
    time.sleep(2)


