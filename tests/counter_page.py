class CounterPage:
    def __init__(self,page):
        self.page=page

    def visit(self):
        self.page.goto('https://counter.onlineclock.net/')

    def get_count_down_button(self):
        return self.page.locator('text="Count Down"')

    def get_count_up_button(self):
        return self.page.locator('text="Count Up"')

    def count_down(self):
        locator=self.get_count_down_button()
        locator.click()

    def count_up(self):
        locator=self.get_count_up_button()
        locator.click()

    def get_current_value(self):
        content=self.page.locator('#counter')
        text=content.text_content()
        return text