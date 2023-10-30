from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_2_implicit_waits(driver):
    """1. Перейти по URL: Открыть в браузере указанный URL сайта "https://victoretc.github.io/selenium_waits/"""
    driver.get('https://victoretc.github.io/selenium_waits/')

    """2. Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium"."""
    title_text = driver.find_element(By.XPATH, '//h1').text
    assert title_text == 'Практика с ожиданиями в Selenium'

    """3. Дождаться появления кнопки "Начать тестирование" """
    """4. Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование"."""
    visible_button_start_test = driver.find_element(By.XPATH, '// button[@id ="startTest" and not (contains(@class, "hidden"))]')
    assert visible_button_start_test.is_displayed()

    """5. Начать тестирование: Кликнуть по кнопке "Начать тестирование"."""
    visible_button_start_test.click()

    """6. Ввод логина: Ввести "login" в поле для логина."""
    login = driver.find_element(By.XPATH, "//input[@id='login']")
    value_login = login.send_keys('Nata')

    """7. Ввод пароля: Ввести "password" в поле для пароля."""
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    value_password = password.send_keys('123')

    """8. Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами"."""
    agree_check_box = driver.find_element(By.XPATH, "//input[@id='agree']")
    agree_check_box.click()

    """9. Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться"."""
    register = driver.find_element(By.XPATH, "// button[@id = 'register']")
    register.click()

    """10. Проверка загрузки: Удостовериться, что появился индикатор загрузки."""
    visible_loader = driver.find_element(By.XPATH,"//div[@id ='loader' and not (contains(@class, 'hidden'))]")
    assert visible_loader.is_displayed()

    """11. Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы"."""
    success_message = driver.find_element(By.XPATH, "//p[@id ='successMessage' and not (contains(@class, 'hidden'))]")
    assert success_message.text == 'Вы успешно зарегистрированы!'
