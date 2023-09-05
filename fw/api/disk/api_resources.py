from fw.api.api_base import ApiBase


class ApiResources(ApiBase):

    'Список опубликованных ресурсов'
    def get_resources_public(self, params=None):
        return self.requests_GET(self.get_base_url() + 'resources/last-uploaded', params)

    'Авторизация'
    def post_login(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'login', body, params)

    "Создать папку"
    def put_resources(self, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'resources?path={body}', params)

    'Получить список файлов упорядоченный по имени'
    def get_resources_files(self, params=None):
        return self.requests_GET(self.get_base_url() + 'resources/files', params)
