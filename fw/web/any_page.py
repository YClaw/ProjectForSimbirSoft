from selenium.webdriver.common.by import By

from fw.web.web_base import WebBase


class Locator:
    btn_disk = (By.XPATH, '//a[contains(@class, "serviceDiskButton")]')
    btn_mail = (By.XPATH, '//a[contains(@data-statlog, "headline.mail")]')
    btn_enter = (By.XPATH, '//a[contains(@data-statlog, "headline.enter")]')
    btn_user_avatar = (By.XPATH, '//a[contains(@data-statlog, "headline.avatar")]')


class AnyPage(WebBase):

    'Нажимаем на кнопку "Войти" на главной странице'
    def click_btn_sign_in_on_main_page(self):
        return self.click_element(Locator.btn_enter)

    'Перейти на страницу "Почта"'
    def open_mail(self):
        return self.click_element(Locator.btn_mail)

    'Перейти на страницу "Диск"'
    def open_disk(self):
        return self.click_element(Locator.btn_disk)
