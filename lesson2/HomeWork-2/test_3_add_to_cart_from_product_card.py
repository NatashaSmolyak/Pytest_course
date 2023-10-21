from selenium.webdriver.common.by import By
import time
from locators import  PRODUCT_1, PRICE_PRODUCT_1, SELECT_PRODUCT_1, SHOPPING_CART,\
    CART_PRODUCT_1, PRICE_CART_PRODUCT_1, PRODUCT_CARD, PRICE_CARD

# 3. Добавление товара в корзину из карточки товара
def test_add_to_cart_from_product_card(driver, login):
    """Информация о Продукте 1 в каталоге"""
    product_1 = driver.find_element(By.XPATH, PRODUCT_1)
    value_product_1 = product_1.text
    price_product_1 = driver.find_element(By.XPATH, PRICE_PRODUCT_1)
    value_price_product_1 = price_product_1.text
    """Переход в карточку товара"""
    product_1.click()
    time.sleep(2)
    """Информация о Продукте 1 в карточке товара. Проверка"""
    product_1_card = driver.find_element(By.XPATH, PRODUCT_CARD)
    value_product_1_card = product_1_card.text
    assert value_product_1_card == value_product_1
    price_product_1_card = driver.find_element(By.XPATH, PRICE_CARD)
    value_price_product_1_card = price_product_1_card.text
    assert value_price_product_1_card == value_price_product_1
    time.sleep(2)

    """Добавление Продукта 1 в корзину"""
    select_product_1 = driver.find_element(By.XPATH, SELECT_PRODUCT_1)
    select_product_1.click()
    time.sleep(2)

    """Переход в корзину"""
    cart = driver.find_element(By.XPATH, SHOPPING_CART)
    cart.click()
    time.sleep(3)

    """Информация о Продукте 1 в корзине. Проверка"""
    cart_product_1 = driver.find_element(By.XPATH, CART_PRODUCT_1)
    value_cart_product_1 = cart_product_1.text
    assert value_product_1_card == value_cart_product_1
    price_cart_product_1 = driver.find_element(By.XPATH, PRICE_CART_PRODUCT_1)
    value_cart_price_product_1 = price_cart_product_1.text
    assert value_price_product_1_card == value_cart_price_product_1

