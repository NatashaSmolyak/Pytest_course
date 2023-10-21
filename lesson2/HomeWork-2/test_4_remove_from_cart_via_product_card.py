from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from locators import  PRODUCT_1, PRICE_PRODUCT_1, SELECT_PRODUCT_1, SHOPPING_CART,\
    CART_PRODUCT_1, PRICE_CART_PRODUCT_1, PRODUCT_CARD, PRICE_CARD

# 4. Удаление товара из корзины через карточку товара
# Проверка, что элемент отсутствует на странице.
def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return True
    return False
def test_remove_from_cart_via_product_card(driver, login):
    """Информация о Продукте 1 в каталоге"""
    product_1 = driver.find_element(By.XPATH, PRODUCT_1)
    value_product_1 = product_1.text
    price_product_1 = driver.find_element(By.XPATH, PRICE_PRODUCT_1)
    value_price_product_1 = price_product_1.text
    """Добавление Продукта 1 в корзину"""
    select_product_1 = driver.find_element(By.XPATH, SELECT_PRODUCT_1)
    select_product_1.click()
    time.sleep(2)
    """Переход в корзину"""
    cart = driver.find_element(By.XPATH, SHOPPING_CART)
    cart.click()
    time.sleep(2)
    """Информация о Продукте 1 в корзине. Проверка"""
    cart_product_1 = driver.find_element(By.XPATH, CART_PRODUCT_1)
    value_cart_product_1 = cart_product_1.text
    assert value_product_1 == value_cart_product_1
    price_cart_product_1 = driver.find_element(By.XPATH, PRICE_CART_PRODUCT_1)
    value_cart_price_product_1 = price_cart_product_1.text
    assert value_price_product_1 == value_cart_price_product_1
    """Переход в карточку товара"""
    cart_product_1.click()
    time.sleep(2)
    """Информация о Продукте 1 в карточке товара. Проверка"""
    product_1_card = driver.find_element(By.XPATH, PRODUCT_CARD)
    value_product_1_card = product_1_card.text
    assert value_product_1_card == value_cart_product_1
    price_product_1_card = driver.find_element(By.XPATH, PRICE_CARD)
    value_price_product_1_card = price_product_1_card.text
    assert value_price_product_1_card == value_cart_price_product_1
    time.sleep(2)

    # Удаление из корзины
    remove = driver.find_element(By.XPATH, "//button[@data-test = 'remove-sauce-labs-backpack']")
    remove.click()

    # Проверяем появление кнопки "Add to cart"
    button_add = driver.find_element(By.XPATH, "// button[@ id = 'add-to-cart-sauce-labs-backpack']")
    assert button_add

    # Переход в корзину
    shopping_cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    shopping_cart.click()
    time.sleep(2)

    # Проверяем, что товара нет в корзине.
    removed = check_exists_by_xpath('//*[@id="item_4_title_link"]/div')

    assert removed == True






