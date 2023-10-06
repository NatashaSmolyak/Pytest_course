from selenium import webdriver
import time
import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
def test_smoke():
    base_url = 'https://www.saucedemo.com/'
    driver.get(base_url)
    driver.maximize_window()

    login_standard_user = "standard_user"
    password_all = "secret_sauce"

    user_name = driver.find_element(By.XPATH, "//input[@ID='user-name']")
    user_name.send_keys(login_standard_user)
    print("Input Login")
    password = driver.find_element(By.XPATH, "//input[@ID='password']")
    password.send_keys(password_all)
    print("Input Password")
    login_button = driver.find_element(By.XPATH, "//input[@ID='login-button']")
    login_button.click()
    print("Click Login Button")
    time.sleep(2)

    """ INFO PRODUCT №1"""
    product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
    value_product_1 = product_1.text
    print(value_product_1)

    price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    value_price_product_1 = price_product_1.text
    print(value_price_product_1)

    select_product_1 = driver.find_element(By.XPATH, "//button[@id ='add-to-cart-sauce-labs-backpack']")
    select_product_1.click()
    print("Select Product 1")

    cart = driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']")
    cart.click()
    print("Enter Cart")

    """ INFO Cart Product №1"""
    cart_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
    value_cart_product_1 = cart_product_1.text
    print(value_cart_product_1)
    assert value_product_1 == value_cart_product_1
    print('INFO Cart Product 1 GOOD')

    price_cart_product_1 = driver.find_element(By.XPATH,
                                               '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
    value_cart_price_product_1 = price_cart_product_1.text
    print(value_cart_price_product_1)
    assert value_price_product_1 == value_cart_price_product_1
    print('INFO Cart Price Product 1 GOOD')

    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout.click()
    print('Checkout Click')

    """ Select User INFO"""
    first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
    first_name.send_keys('Nata')
    print("Input First Name")

    last_name = driver.find_element(By.XPATH, "//input[@ID='last-name']")
    last_name.send_keys('Smol')
    print("Input Last Name")

    zip_postal_code = driver.find_element(By.XPATH, "//input[@ID='postal-code']")
    zip_postal_code.send_keys(123456)
    print("Input Zip/Postal Code")

    button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
    button_continue.click()
    print('Continue Click')
    time.sleep(3)

    """INFO Finish Product1"""
    finish_product_1 = driver.find_element(By.XPATH, "//a[@id ='item_4_title_link']")
    value_finish_product_1 = finish_product_1.text
    print(value_finish_product_1)
    assert value_product_1 == value_finish_product_1
    print('INFO Finish Product 1 GOOD')

    finish_price_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    value_finish_price_product_1 = finish_price_product_1.text
    assert value_price_product_1 == value_finish_price_product_1
    print('INFO Finish Price Product 1 GOOD')

    summary_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
    value_summary_price = summary_price.text
    print(value_summary_price)
    item_total = "Item total: " + value_finish_price_product_1
    print(item_total)
    assert value_summary_price == item_total
    print("Total summary price GOOD")