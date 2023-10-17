from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_browser(self):
        self.driver.get(self.url)

    def drag_and_drop(self, drag, drop):
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop)
        action.perform()

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_presence(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
