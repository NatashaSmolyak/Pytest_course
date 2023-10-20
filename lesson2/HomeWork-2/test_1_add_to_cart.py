from selenium.webdriver.common.by import By
import time
from locators import  PRODUCT_1, PRICE_PRODUCT_1, SELECT_PRODUCT_1, SHOPPING_CART, CART_PRODUCT_1, PRICE_CART_PRODUCT_1

# 1. Добавление товара в корзину через каталог
def test_add_to_cart_product_1(driver, login):
    """Информация о Продукте 1 в каталоге"""
    product_1 = driver.find_element(By.XPATH, PRODUCT_1)
    value_product_1 = product_1.text
    price_product_1 = driver.find_element(By.XPATH, PRICE_PRODUCT_1)
    value_price_product_1 = price_product_1.text
    """Добавление Продукта 1 в корзину"""
    select_product_1 = driver.find_element(By.XPATH, SELECT_PRODUCT_1)
    select_product_1.click()
    """ Переход в корзину"""
    cart = driver.find_element(By.XPATH, SHOPPING_CART)
    cart.click()
    time.sleep(3)
    """Информация о Продукте 1 в корзине. Проверка"""
    cart_product_1 = driver.find_element(By.XPATH, CART_PRODUCT_1)
    value_cart_product_1 = cart_product_1.text
    assert value_product_1 == value_cart_product_1
    price_cart_product_1 = driver.find_element(By.XPATH, PRICE_CART_PRODUCT_1)
    value_cart_price_product_1 = price_cart_product_1.text
    assert value_price_product_1 == value_cart_price_product_1



