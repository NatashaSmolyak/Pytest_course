import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON,  PRODUCT_1, PRICE_PRODUCT_1,\
    SELECT_PRODUCT_1, SHOPPING_CART, CART_PRODUCT_1, PRICE_CART_PRODUCT_1
from data import LOGIN_VALID, PASSWORD_VALID, MAIN_PAGE, INVENTORY_PAGE

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def login(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN_VALID)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD_VALID)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    assert driver.current_url == INVENTORY_PAGE

@pytest.fixture()
def cart(driver, login):
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