from selenium.webdriver.common.by import By

class InteractionsLocators:
    DRAG = (By.CSS_SELECTOR, "div[id='draggable']")
    DROP = (By.CSS_SELECTOR, "div[id='droppable']")
    DROP_TEXT = (By.CSS_SELECTOR, "div[id='droppable']>p")