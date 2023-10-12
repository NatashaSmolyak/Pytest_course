# 1. Проверка работоспособности фильтра (A to Z)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

driver = webdriver.Chrome()

def test_filter_1():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # Формируем изначальный список продуктов на странице
    items_before = driver.find_elements(By.XPATH, '//*[@class="inventory_item_name "]')
    # Парсим названия продуктов в список
    items_name_before = [items_before[i].text for i in range(len(items_before))]
    # Сортируем список по возрастанию
    sort_items_name_asc_before = sorted(items_name_before, key=lambda x: items_name_before[0])
    time.sleep(3)

    # Фильтрация с помощью Keys.DOWN от Z-A. Это предусловие.
    filter = driver.find_element(By.XPATH, "//select[@data-test ='product_sort_container']")
    filter.click()
    time.sleep(1)
    filter.send_keys(Keys.DOWN)
    time.sleep(1)
    filter.send_keys(Keys.RETURN)
    time.sleep(2)

    # Фильтрация с помощью Keys.UP от A-Z
    filter = driver.find_element(By.XPATH, "//select[@data-test ='product_sort_container']")
    filter.click()
    time.sleep(1)
    filter.send_keys(Keys.UP)
    time.sleep(1)
    filter.send_keys(Keys.RETURN)
    time.sleep(2)

    # Формируем список продуктов после использования фильтра A-Z
    sort_items_asc_after = driver.find_elements(By.XPATH, '//*[@class="inventory_item_name "]')
    # Формируем список из названий продуктов
    sort_items_name_asc_after = [sort_items_asc_after[i].text for i in range(len(sort_items_asc_after))]
    # Сравниваем два списка
    assert sort_items_name_asc_before == sort_items_name_asc_after
    time.sleep(2)


