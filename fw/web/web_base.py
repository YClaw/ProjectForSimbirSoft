from fw.fw_base import FWBase

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class WebBase(FWBase):

    def GetDriver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.driver = self.manager.driver_instance.get_driver(self)
        return self.manager.driver_instance.driver

    def open_main_page(self):
        main_page = self.manager.settings.GLOBAL['Yandex']['Link']
        self.GetDriver().get(main_page)

    def move_to_element(self, locator):
        actions = ActionChains(self.GetDriver())
        element = self.GetDriver().find_element(locator)
        actions.move_to_element(element)
        actions.perform()
        return self

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
        return self

    def find_element(self, locator, wait=30):
        web_element = WebDriverWait(self.GetDriver(), wait).until(
            expected_conditions.presence_of_element_located(locator))
        return web_element

    def get_tag_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def send_keys(self, locator, text):
        web_element = self.find_element(locator)
        web_element.send_keys(text)

    def move_to_last_page_in_browser(self):
        pages = self.GetDriver().window_handles
        self.GetDriver().switch_to.window(pages[-1])
        return self

    def right_click(self, locator):
        actions = ActionChains(self.GetDriver())
        element = self.find_element(locator)
        actions.context_click(element).perform()
        return self

    def double_click(self, locator):
        actions = ActionChains(self.GetDriver())
        actions.double_click(self.find_element(locator)).perform()

    def close_current_page(self):
        pages = self.GetDriver().window_handles
        self.GetDriver().close()
        return self

    def find_elements(self, locator, wait=30):
        web_element = WebDriverWait(self.GetDriver(), wait).until(
            expected_conditions.presence_of_all_elements_located(locator))
        return web_element
