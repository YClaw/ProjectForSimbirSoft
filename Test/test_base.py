from fw.application_manager import ApplicationManager
from data.settings import Settings

class TestBase:

    manager = ApplicationManager()
    yandex_main_page = Settings.GLOBAL['Yandex']['Link']

    def setup_class(self):
        pass

    def setup_method(self):
        pass

    def teardown_module(self):
        pass

    def teardown_class(self):
        pass
