from Test.api_tests.api_base import ApiBase


class TestAPIResources(ApiBase):

    'Получаем список файлов на диске (Файлов на диске 7)'
    def test_get_files_on_disk(self):
        # Получаем файлы
        files = self.manager.api_resources.get_resources_files()
        # Сравниваем количество файлов
        assert len(files['items']) == 7
        # Проверяем статус ответа
        assert self.manager.group_data.response.status_code == 200
