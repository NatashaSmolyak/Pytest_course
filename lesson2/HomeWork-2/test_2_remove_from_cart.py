from selenium.webdriver.common.by import By
from locators import  REMOVE_CART_PRODUCT_1


# 2. Удаление товара из корзины через корзину
def test_add_product_1(driver, login, cart):
    """ Удаление из корзины"""
    remove_product_1 = driver.find_element(By.XPATH, REMOVE_CART_PRODUCT_1)
    remove_product_1.click()
    # Сохранение в переменную removed наличие класса removed_cart_item
    removed = driver.find_element(By.CSS_SELECTOR, ".removed_cart_item")
    assert removed