from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
# Проверка, что элемент отсутствует на странице.
def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return True
    return False

driver = webdriver.Chrome()

# 3. Удаление товара из корзины через карточку товара
def test_remove_item_from_cart():
    driver.get("https://www.saucedemo.com/")
    # Авторизация
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(2)
    # Сохранение в переменную name_item_main названия добавляемого товара
    name_item_main = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link']>div[class='inventory_item_name ']").text
    print(name_item_main)
    # Добавление в корзину
    button_add = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    button_add.click()
    time.sleep(2)

    # Переход в корзину
    shopping_cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    shopping_cart.click()
    time.sleep(2)

    # Сохранение в переменную name_item_shopping_cart названия добавленного товара
    name_item_shopping_cart = driver.find_element(By.CSS_SELECTOR, "a[id = 'item_4_title_link'] > div[class='inventory_item_name']").text

    # Проверяем, что добавился нужный товар
    assert name_item_main == name_item_shopping_cart

    # Переход в карточку товара
    link_item_title = driver.find_element(By.CSS_SELECTOR, "a[id = 'item_4_title_link'] > div[class='inventory_item_name']")
    link_item_title.click()
    time.sleep(2)

    # Сохранение в переменную name_item_card названия товара, прописанное в карточке
    name_item_card = driver.find_element(By.XPATH, " //div[@class='inventory_details_name large_size']").text
    time.sleep(2)

    # Проверяем, что открылась карточка нужного товара
    assert name_item_shopping_cart == name_item_card

    # Удаление из корзины
    remove = driver.find_element(By.XPATH, "//button[@data-test = 'remove-sauce-labs-backpack']")
    remove.click()

    #Проверяем появление кнопки "Add to cart"
    button_add = driver.find_element(By.XPATH, "// button[@ id = 'add-to-cart-sauce-labs-backpack']")
    assert button_add

    # Переход в корзину
    shopping_cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    shopping_cart.click()
    time.sleep(2)

    # Проверяем, что товара нет в корзине.
    removed = check_exists_by_xpath('//*[@id="item_4_title_link"]/div')

    assert removed == True


