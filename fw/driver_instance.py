from selenium import webdriver


class DriverInstance:

    driver = None

    def get_driver(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.driver.set_script_timeout(600)
        self.driver.set_page_load_timeout(600)

        return self.driver
