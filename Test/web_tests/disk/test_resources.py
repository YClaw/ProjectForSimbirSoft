import datetime

now = datetime.datetime.now()

from Test.web_tests.web_base import WebBase

'Тесты на создание файлов на диске'
class TestResources(WebBase):

    def setup_method(self):
        # Переходим на страницу "Диск"
        self.manager.any_page.open_disk()

    'Создание нового файла в новой папке'
    def test_create_new_file_in_new_folder(self):
        folder_name = 'AutotestFolder ' + now.strftime("%d.%m.%Y %H:%M")
        file_name = 'AutotestFile ' + now.strftime("%d.%m.%Y %H:%M")
        # Создаем папку
        self.manager.web_disk_create.create_folder_use_right_click(folder_name)
        # Переходим в папку
        self.manager.web_disk_create.open_folder_by_name(folder_name)
        # Создаем файл
        self.manager.web_disk_create.create_file_use_right_click(file_name, file_type=1)
        # Переходим на последнюю вкладку и закрываем её
        self.manager.web_base.move_to_last_page_in_browser()
        self.manager.web_base.close_current_page()
        # Получаем список файлов
        self.manager.web_base.move_to_last_page_in_browser()
        files = self.manager.web_disk_create.get_files_list()
        # Проверяем, что в папке 1 файл и его название
        assert len(files) == 1
        assert file_name in files
