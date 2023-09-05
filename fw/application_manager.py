from data.group_data import GroupData
from data.settings import Settings

from fw.fw_base import FWBase
from fw.driver_instance import DriverInstance

from fw.api.api_token import ApiToken
from fw.api.api_base import ApiBase

from fw.web.any_page import AnyPage
from fw.web.login import Login
from fw.web.web_base import WebBase

from fw.api.disk.api_resources import ApiResources

from fw.web.disk.disk_create import WebDiskCreate


class ApplicationManager:

    settings = Settings()
    group_data = GroupData()

    def __init__(self):
        self.fw_base = FWBase(self)
        self.driver_instance = DriverInstance

        self.api_base = ApiBase(self)
        self.api_token = ApiToken(self)

        self.web_base = WebBase(self)
        self.any_page = AnyPage(self)
        self.login = Login(self)

        self.api_resources = ApiResources(self)

        self.web_disk_create = WebDiskCreate(self)
