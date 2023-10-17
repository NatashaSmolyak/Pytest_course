from lesson2.locators.locators_interactions import InteractionsLocators
from lesson2.pages.base_page import BasePage

class InteractionPage(BasePage):
    locator = InteractionsLocators

    def drag_simple(self):
        drag_div = self.element_is_visible(self.locator.DRAG)
        drop_div = self.element_is_visible(self.locator.DROP)
        self.drag_and_drop(drag_div, drop_div)
        text = self.element_is_visible(self.locator.DROP_TEXT).text
        return text