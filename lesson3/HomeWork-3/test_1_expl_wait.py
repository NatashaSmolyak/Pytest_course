from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait

def test_1_explicit_waits(driver, wait):
    """1. Перейти по URL: Открыть в браузере указанный URL сайта "https://victoretc.github.io/selenium_waits/"""
    driver.get('https://victoretc.github.io/selenium_waits/')

    """2. Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium"."""
    title_text = driver.find_element(By.XPATH, '//h1').text
    assert title_text == 'Практика с ожиданиями в Selenium'

    """3. Дождаться появления кнопки "Начать тестирование" """
    """4. Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование"."""
    visible_button_start_test = wait.until(EC.element_to_be_clickable((By.XPATH, '// button[@id ="startTest"]')))
    assert visible_button_start_test.text == 'Начать тестирование'

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
    visible_loader = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id ='loader']")))
    assert visible_loader.is_displayed()

    """11. Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы"."""
    success_message = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//p[@id ='successMessage']"), 'Вы успешно зарегистрированы!'))
    assert success_message
