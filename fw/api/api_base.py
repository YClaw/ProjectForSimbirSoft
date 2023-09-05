from json.decoder import JSONDecodeError

from fw.fw_base import FWBase

import requests

class ApiBase(FWBase):

    def get_base_url(self):
        return self.manager.settings.GLOBAL['Yandex']['API']['Link']

    def get_headers(self, application_json=True, headers=None, accept=False):
        if headers is None:
            headers = {}
        else:
            return headers

        if self.manager.settings.Authorization:
            headers['Authorization'] = self.manager.group_data.token

        if accept is True:
            headers['accept'] = 'application/json'

        if application_json:
            headers['accept'] = 'application/json'
            headers['Content-Type'] = 'application/json'

        return headers

    def requests_GET(self, url, params=None):
        headers = self.get_headers()

        response = requests.get(url, headers=headers, params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'

        try:
            return response.json()
        except JSONDecodeError:
            return response

    def requests_POST(self, url, body, params=None):
        headers = self.get_headers()

        response = requests.post(url, headers=headers, data=body, params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'

        try:
            return response.json()
        except JSONDecodeError:
            return response

    def requests_PUT(self, url, body, params=None):
        headers = self.get_headers()

        responce = requests.put(url, headers=headers, data=body, params=params)
        self.manager.group_data.response = responce

        responce.encoding = 'utf-8'

        try:
            return responce.json()
        except JSONDecodeError:
            return responce

    def requests_PATCH(self, url, body, params=None):
        headers = self.get_headers()

        responce = requests.patch(url, headers=headers, data=body, params=params)
        self.manager.group_data.response = responce

        responce.encoding = 'utf-8'

        try:
            return responce.json()
        except JSONDecodeError:
            return responce

    def requests_DELETE(self, url, params=None):
        headers = self.get_headers()

        response = requests.delete(url, headers=headers, params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'

        try:
            return response.json()
        except JSONDecodeError:
            return response
