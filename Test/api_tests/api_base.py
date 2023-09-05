from Test.test_base import TestBase

class ApiBase(TestBase):

    def setup_class(self):
        pass

    def setup_method(self):
        self.manager.api_token.get_token()

    def teardown_class(self):
        pass

    def teardown_method(self):
        pass
