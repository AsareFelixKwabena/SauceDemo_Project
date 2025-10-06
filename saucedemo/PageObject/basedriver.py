from selenium import webdriver


class BaseDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        def quit_driver(self):
            self.driver.quit()


def get_driver(self):
    return self.driver()
