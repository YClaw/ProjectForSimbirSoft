from Test.test_base import TestBase

class WebBase(TestBase):

    def setup_class(self):
        self.manager.web_base.open_main_page()
        self.manager.any_page.click_btn_sign_in_on_main_page()
        self.manager.login.login_by_log_pass()
        self.manager.any_page.open_mail()
        # После открытия почты переходим на последнюю вкладку
        self.manager.web_base.move_to_last_page_in_browser()

    def setup_method(self):
        pass

    def teardown_class(self):
        self.manager.driver_instance.driver.quit()
        self.manager.driver_instance.driver.stop_client()

    def teardown_method(self):
        self.manager.login.log_out()
