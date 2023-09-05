from fw.api.api_base import ApiBase


class ApiToken(ApiBase):

    'Отправляем Токен нужного пользователя'
    def get_token(self, user_name='TestLapaev'):

        self.manager.group_data.token = self.manager.group_data.users[user_name]['token']

        return self
