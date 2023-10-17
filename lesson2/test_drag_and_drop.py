from lesson2.pages.interactions_page import InteractionPage

class TestInteraction:

    def test_drag_and_drop(self, driver):
        page = InteractionPage(driver, "https://demoqa.com/droppable")
        page.open_browser()
        text = page.drag_simple()
        assert text == 'Dropped!'
